import pickle
from classes.data import get_training_data, get_verification_data
from classes.xlsxReader import read_data_from_file
import numpy as np
from sklearn import metrics
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

data = read_data_from_file("data.pkl")

static_train, static_target = get_training_data(data)
dynamic_train, dynamic_target = get_verification_data(data)

with open("model.pkl", "rb") as f:
    clf: MLPRegressor = pickle.load(f)


def stats(train, target):
    print(f"r2_score: {metrics.r2_score(target, train)}")
    print(
        f"explained_variance_score: {metrics.explained_variance_score(target, train)}")
    print(
        f"mean_absolute_error: {metrics.mean_absolute_error(target, train)}")
    print(
        f"mean_squared_error: {metrics.mean_squared_error(target, train)}")
    print(
        f"median_absolute_error: {metrics.median_absolute_error(target, train)}")
    print(
        f"mean_squared_log_error: {metrics.mean_squared_log_error(target, train)}")
    # print(
    #     f"accuracy_score: {metrics.accuracy_score(target, train)}")


###############################################################################
# Static
###############################################################################
print("#############################")
print("# Static:")
print("amount of data:", len(static_train))
static_read = []
for i in range(len(static_train)):
    l = len(static_train[i])
    # print(static_train[i])
    # print([static_train[i][l-3], static_train[i][l-2]])
    static_read.append([static_train[i][l-3], static_train[i][l-2]])
static_predicts = clf.predict(static_train)
static_target = np.array(static_target)
stats(static_predicts, static_target)


###############################################################################
# Dynamiczne
###############################################################################

dynamic_read = []
for i in range(len(dynamic_train)):
    l = len(dynamic_train[i])
    # print(dynamic_train[i])
    # print([dynamic_train[i][l-3], dynamic_train[i][l-2]])
    dynamic_read.append([dynamic_train[i][l-3], dynamic_train[i][l-2]])

dynamic_predicts = clf.predict(dynamic_train)
dynamic_target = np.array(dynamic_target)

print("\n######################################")
print("# Dynamic:")
print("amount of data:", len(dynamic_train))
stats(dynamic_predicts, dynamic_target)

# rotate all data 90 degrees
dynamic_read = np.rot90(dynamic_read)
dynamic_predicts = np.rot90(dynamic_predicts)
dynamic_target = np.rot90(dynamic_target)


plt.title("Dynamic")
plt.scatter(dynamic_predicts[0], dynamic_predicts[1],
            c='red', label='predicted', s=1)
plt.scatter(dynamic_read[0], dynamic_read[1], c='blue', label='read', s=1)
plt.scatter(dynamic_target[0], dynamic_target[1],
            c='green', label='target', s=1)
plt.legend()
plt.savefig("dynamic.png")

plt.title("Static")
plt.scatter(static_predicts[0], static_predicts[1],
            c='red', label='predicted', s=1)
plt.scatter(static_read[0], static_read[1], c='blue', label='read', s=1)
plt.scatter(static_target[0], static_target[1],
            c='green', label='target', s=1)
# plt.legend()
plt.savefig("static.png")
