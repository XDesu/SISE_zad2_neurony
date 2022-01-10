from classes.xlsxReader import DATA_LABELS


def get_training_data(data):
    static_train = []
    static_target = []
    # last_len = 0
    for room in ["f10", "f8"]:
        for key, val in enumerate(data[room]["static"]["s"]):
            for i in range(len(val)):
                tmp_train = list(val[i].values())
                tmp_target = tmp_train[-2:]
                tmp_train = tmp_train[:-2]

                if any(x in tmp_train for x in [None, ""]):
                    continue

                if (len(tmp_train) != len(DATA_LABELS) - 2):
                    tmp_train.pop()
                static_train.append(tmp_train)
                static_target.append(tmp_target)
    return static_train, static_target


def get_verification_data(data):
    dynamic_train = []
    dynamic_target = []
    for room in ["f10", "f8"]:
        for data_type in ["dynamic", "random"]:
            for turn in ["p", "z"]:
                for key, val in enumerate(data[room][data_type][turn]):
                    for i in range(len(val)):
                        tmp_train = list(val[i].values())
                        tmp_target = tmp_train[-2:]
                        tmp_train = tmp_train[:-2]

                        if any(x in tmp_train for x in [None, ""]):
                            continue

                        if (len(tmp_train) != len(DATA_LABELS) - 2):
                            continue
                        dynamic_train.append(tmp_train)
                        dynamic_target.append(tmp_target)

    return dynamic_train, dynamic_target
