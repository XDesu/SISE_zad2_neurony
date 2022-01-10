import pickle
from classes.data import get_training_data, get_verification_data
from classes.xlsxReader import read_data_from_file
import numpy as np
from sklearn import metrics
from sklearn.neural_network import MLPRegressor

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
predicts = clf.predict(static_train)
static_target = np.array(static_target)
stats(predicts, static_target)

# print("###################")
# print("read:")
# print([static_train[0][-3], static_train[0][-2]])
# print("predict:")
# print(clf.predict([static_train[0]]))
# print("target:")
# print(static_target[0])

###############################################################################
# Dynamiczne
###############################################################################


predicts = clf.predict(dynamic_train)
dynamic_target = np.array(dynamic_target)
# targets = np.array(dynamic_target)
# diff = np.subtract(predicts, targets)
# squar = np.square(diff)
# mse = squar.mean()

print("\n######################################")
print("# Dynamic:")
print("amount of data:", len(dynamic_train))
stats(predicts, dynamic_target)

# print("Dynamiczne wyniki:")


# # print("###################")
# print("read:")
# print([dynamic_train[0][-3], dynamic_train[0][-2]])
# print("predict:")
# print(clf.predict([dynamic_train[0]]))
# print("target:")
# print(dynamic_target[0])
