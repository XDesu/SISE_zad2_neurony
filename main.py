from classes.xlsxReader import smart_read
from os.path import isfile, join
from os import listdir

F8 = [f for f in listdir('pomiary/F8') if isfile(join('pomiary/F8', f))]
F10 = [f for f in listdir('pomiary/F10') if isfile(join('pomiary/F10', f))]
ROOMS = F8 + F10

data = smart_read(ROOMS, "data.pkl")
# print(data["f10"]["dynamic"]["p"][1][10]["Unnamed: 0"])
