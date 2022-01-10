from classes.xlsxReader import smart_read, DATA_LABELS
from os.path import isfile, join
from os import listdir
from sklearn.neural_network import MLPClassifier, MLPRegressor
import numpy as np

F8 = [f for f in listdir('pomiary/F8') if isfile(join('pomiary/F8', f))]
F10 = [f for f in listdir('pomiary/F10') if isfile(join('pomiary/F10', f))]
ROOMS = F8 + F10


# data = read_xlsx('pomiary/F8/' + F8[0])
# print(data[1][None])
data = smart_read(ROOMS, "data2.pkl")
# print(data["f10"]["dynamic"]["p"][1][10][None])


f10_static_train = []
f10_static_target = []
# last_len = 0
for room in ["f10", "f8"]:
    for key, val in enumerate(data[room]["static"]["s"]):
        for i in range(len(val)):
            tmp_train = list(val[i].values())
            tmp_target = tmp_train[-2:]
            tmp_train = tmp_train[:-2]

            if any(x in tmp_train for x in [None, ""]):
                continue

            # if last_len != len(tmp_train):
            #     print(tmp_train)
            #     last_len = len(tmp_train)

            if (len(tmp_train) != len(DATA_LABELS) - 2):
                tmp_train.pop()
            f10_static_train.append(tmp_train)
            f10_static_target.append(tmp_target)

            # f10_static_train.append(list(val[i].values()))
            # f10_static_target.append(f10_static_train[-1][-2:])
            # f10_static_train[-1] = f10_static_train[-1][:-2]


# [1609326843.033, -0.0625, -0.0625, 0, 15.5625, -16, -46, 0.07769775390625, -0.03594970703125, -0.97381591796875, -0.21051025390625, 11, 1, 9, 0, 0, -149, 38, 971, 3.567, -0.167, -0.037, 38.6, 28.334, 28.334, 7586, 1089, 1000]

# for i in range(len(f10_static_train)):
#     tmp = len(f10_static_train[i])
#     if tmp != 4:
#         print(f10_static_train[i])
# np.asarray(f10_static_train, dtype=float)


# 29 warstw
# 2 * 29 = 58
layers = (28, 17, 17, 12, 2)
clf = MLPRegressor(
    solver='adam', alpha=1e-4, tol=1e-6, hidden_layer_sizes=layers,
    random_state=1, max_iter=1000, verbose=True, epsilon=1e-9,
)
clf.fit(f10_static_train, f10_static_target)
print("###################")
print("read:")
print([f10_static_train[0][-3], f10_static_train[0][-2]])
print("predict:")
print(clf.predict([f10_static_train[0]]))
print("target:")
print(f10_static_target[0])

# predicts = clf.predict(f10_static_train)
print("Wynik:")
print(clf.score(f10_static_train, f10_static_target))
