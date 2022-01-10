import pickle
from classes.xlsxReader import smart_read, DATA_LABELS
from os.path import isfile, join
from os import listdir
from sklearn.neural_network import MLPRegressor
from classes.data import get_training_data, get_verification_data
import numpy as np
import random

F8 = [f for f in listdir('pomiary/F8') if isfile(join('pomiary/F8', f))]
F10 = [f for f in listdir('pomiary/F10') if isfile(join('pomiary/F10', f))]
ROOMS = F8 + F10


# data = read_xlsx('pomiary/F8/' + F8[0])
# print(data[1][None])
data = smart_read(ROOMS, "data.pkl")
# print(data["f10"]["dynamic"]["p"][1][10][None])


static_train, static_target = get_training_data(data)
dynamic_train, dynamic_target = get_verification_data(data)


# to_shuffle = list(zip(static_train, static_target))
# random.shuffle(to_shuffle)
# static_train, static_target = zip(*to_shuffle)

# 29 warstw
# 2 * 29 = 58
# layers = (28, 18, 14, 2)  # dopasowanie 99.303%
# layers = (28, 17, 17, 2) # dopasowanie 98.784%
layers = (28, 17, 14, 2)  # dopasowanie 99.482%, iteracji 278
# layers = (28, 20, 17, 2)
clf = MLPRegressor(
    solver='adam', alpha=1e-4, tol=1e-5, hidden_layer_sizes=layers,
    random_state=1, max_iter=1000, verbose=True, epsilon=1e-8,
    activation='relu')


clf.fit(static_train[:50000], static_target[:50000])

# print(clf.out_activation_)

with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)
