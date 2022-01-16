from math import dist
import pickle
from statistics import mean
from classes.data import get_training_data, get_verification_data
from classes.xlsxReader import read_data_from_file
import numpy as np
from sklearn import metrics
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
import os
from prettytable import PrettyTable
from openpyxl import Workbook
import json


OUTPUT_DIR = "output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


with open("model.pkl", "rb") as f:
    clf: MLPRegressor = pickle.load(f)


data = read_data_from_file("data.pkl")

static_train, static_target = get_training_data(data)
static_read = []
for i in range(len(static_train)):
    l = len(static_train[i])
    static_read.append([static_train[i][l-3], static_train[i][l-2]])
static_predicts = clf.predict(static_train)

dynamic_train, dynamic_target = get_verification_data(data)
dynamic_read = []
for i in range(len(dynamic_train)):
    l = len(dynamic_train[i])
    dynamic_read.append([dynamic_train[i][l-3], dynamic_train[i][l-2]])
dynamic_predicts = clf.predict(dynamic_train)


def stats(train, target):

    r2_score = metrics.r2_score(target, train)
    mean_absolute_error = metrics.mean_absolute_error(target, train)
    mean_squared_error = metrics.mean_squared_error(target, train)
    median_absolute_error = metrics.median_absolute_error(target, train)
    mean_absolute_percentage_error = metrics.mean_absolute_percentage_error(
        target, train)
    avg_dist = mean(calc_distances(train, target))

    return \
        f"{round(r2_score*100, 2)}%", \
        round(mean_absolute_error, 2), \
        round(mean_squared_error, 2), \
        round(median_absolute_error, 2), \
        f"{round(mean_absolute_percentage_error*100, 2)}%", \
        round(avg_dist, 2)


def calc_distances(train, target):
    distances = []
    for i in range(len(train)):
        distances.append(dist(train[i], target[i]))
    return distances


table = PrettyTable(["dane", "r2_score", "mean_absolute_error", "mean_squared_error",
                    "median_absolute_error", "mean_absolute_percentage_error", "avg_dist"])
table.add_row(["static_read", *stats(static_read, static_target)])
table.add_row(["static_predict", *stats(static_predicts, static_target)])
table.add_row(["dynamic_read", *stats(dynamic_read, dynamic_target)])
table.add_row(["dynamic_predict", *stats(dynamic_predicts, dynamic_target)])

print(table)


# rotate all data 90 degrees
dynamic_read_rotated = np.rot90(dynamic_read)
dynamic_predicts_rotated = np.rot90(dynamic_predicts)
dynamic_target_rotated = np.rot90(dynamic_target)


plt.title("Dynamic")
plt.scatter(
    dynamic_read_rotated[0], dynamic_read_rotated[1], c='blue', label='read', s=1)
plt.scatter(dynamic_predicts_rotated[0], dynamic_predicts_rotated[1],
            c='red', label='predicted', s=1)
plt.scatter(dynamic_target_rotated[0], dynamic_target_rotated[1],
            c='green', label='target', s=1)

plt.legend()
plt.ylabel("y", loc='top')
plt.xlabel("x", loc='right')

plt.savefig(OUTPUT_DIR + "/dynamic.png")


plt.title("Static")
plt.scatter(static_read[0], static_read[1], c='blue', label='read', s=1)
plt.scatter(static_predicts[0], static_predicts[1],
            c='red', label='predicted', s=1)
plt.scatter(static_target[0], static_target[1],
            c='green', label='target', s=1)
plt.savefig(OUTPUT_DIR + "/static.png")


# zapis średnich odległości do xls
book = Workbook()
sheet = book.active
distances = calc_distances(dynamic_predicts, dynamic_target)
for distance in distances:
    sheet.append([distance])
book.save(OUTPUT_DIR + "/error_distribution.xlsx")


# zapis wag do json
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


with open(OUTPUT_DIR + "/weights.json", "w") as f:
    json.dump(clf.coefs_, f, ensure_ascii=False, indent=2, cls=NumpyEncoder)
