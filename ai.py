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

data = smart_read(ROOMS, "data.pkl")


static_train, static_target = get_training_data(data)
dynamic_train, dynamic_target = get_verification_data(data)


# layers = (17, 14)  # najlepsze wizualnie i mean percentage error
layers = (15)        # identyczne jak wyżej
clf = MLPRegressor(
    solver='adam', alpha=1e-4, tol=1e-5, hidden_layer_sizes=layers,
    random_state=1, max_iter=1000, verbose=True, epsilon=1e-8,
    activation='relu', batch_size=300)

# batch size 300, ponieważ jest to wartość
# która blisko odpowiadała ilości danych per plik


clf.fit(static_train, static_target)


with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)
