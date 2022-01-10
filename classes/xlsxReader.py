from openpyxl import load_workbook
import pickle
from os.path import isfile, join

# DATA_LABELS = [
# 'data__coordinates__x',
# 'data__coordinates__y',
# 'reference__x',
# 'reference__y'
# ]

DATA_LABELS = [
'data__tagData__gyro__x',
'data__tagData__gyro__y',
'data__tagData__gyro__z',
'data__tagData__magnetic__x',
'data__tagData__magnetic__y',
'data__tagData__magnetic__z',
'data__tagData__quaternion__x',
'data__tagData__quaternion__y',
'data__tagData__quaternion__z',
'data__tagData__quaternion__w',
'data__tagData__linearAcceleration__x',
'data__tagData__linearAcceleration__y',
'data__tagData__linearAcceleration__z',
'data__tagData__pressure',
'data__tagData__maxLinearAcceleration',
'data__acceleration__x',
'data__acceleration__y',
'data__acceleration__z',
'data__orientation__yaw',
'data__orientation__roll',
'data__orientation__pitch',
'data__metrics__latency',
'data__metrics__rates__update',
'data__metrics__rates__success',
'data__coordinates__x',
'data__coordinates__y',
'data__coordinates__z',
# 'errorCode',
'reference__x',
'reference__y']

def smart_read(files, file_name):

    # check if file exists
    if isfile(file_name):
        return read_data_from_file(file_name)
    
    # if not, read all files and save to file
    data = read_all(files)
    save_data_to_file(data, file_name)
    return data

def save_data_to_file(data, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)

def read_data_from_file(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)

def read_all(file_names: list[str], path: str = "./pomiary/"):
    data = {}
    data["f8"] = {}
    data["f10"] = {}

    data["f8"]["dynamic"] = {}
    data["f8"]["dynamic"]["p"] = []
    data["f8"]["dynamic"]["z"] = []

    data["f8"]["random"] = {}
    data["f8"]["random"]["p"] = []
    data["f8"]["random"]["z"] = []

    data["f8"]["static"] = {}
    data["f8"]["static"]["s"] = []

    data["f10"]["dynamic"] = {}
    data["f10"]["dynamic"]["p"] = []
    data["f10"]["dynamic"]["z"] = []

    data["f10"]["random"] = {}
    data["f10"]["random"]["p"] = []
    data["f10"]["random"]["z"] = []

    data["f10"]["static"] = {}
    data["f10"]["static"]["s"] = []

    for file_name in file_names:
        parts = file_name.split("_")
        
        room = parts[0]
        measure_type = "static" if parts[1] == "stat" else parts[1]
        direction = "s"
        number = 0
        
        if len(parts) == 2:
            measure_type = "dynamic"

        tmp = parts[-1][:-5]
        if tmp.isdigit():
            number = int(tmp)
        else:
            number = int(tmp[:-1])
            direction = tmp[-1]
        
        path_ext = "F8" if room == "f8" else "F10"
        full_path = path + path_ext + "/" + file_name

        data[room][measure_type][direction].append(read_xlsx(full_path))
    
    return data


def read_xlsx(file_name):
    """
    Reads an xlsx file and returns a list of dictionaries.
    """
    wb = load_workbook(file_name)
    sheet = wb.active
    rows = sheet.rows
    keys = [cell.value for cell in next(rows)]
    # data = [{keys[i]: cell.value for i, cell in enumerate(row)} for row in rows]
    
    data = []
    for row in rows:
        data.append({})
        for i, cell in enumerate(row):
            if keys[i] in DATA_LABELS:
                data[-1][keys[i]] = cell.value
            # if keys[i] not in [None, "Unnamed: 0", "version", "tagId", "data__anchorData"]:
            #     data[-1][keys[i]] = cell.value
                

    return data