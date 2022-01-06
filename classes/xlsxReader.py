from openpyxl import load_workbook
import pickle
from os.path import isfile, join

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
    data = [{keys[i]: cell.value for i, cell in enumerate(row)} for row in rows]
    return data