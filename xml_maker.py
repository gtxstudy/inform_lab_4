def __make_from_dict(data: dict, depth=0):
    result = ""
    indent = "    " * depth
    multilines = False
    for key, val in data.items():
        result += indent + f"<{key.replace(' ', '_')}>"
        if type(val) == dict or type(val) == list:
            result += "\n"
            result += __next_object(val, depth+1)
            multilines = True
        elif type(val) == str:
            result += val
        else:
            raise Exception("Unsupported type")
        result += indent*multilines + f"</{key.replace(' ', '_')}>\n"
    return result


def __make_from_list(data: list, depth=0):
    result = ""
    for item in data:
        if type(item) == dict or type(item) == list:
            result += __next_object(item, depth)
        elif type(item) == str:
            result += item
        else:
            raise Exception("Unsupported type")
    return result


def __next_object(data: dict | list, depth=0):
    result = ""
    if type(data) == dict:
        return __make_from_dict(data, depth)
    elif type(data) == list:
        return __make_from_list(data, depth)
    else:
        raise Exception("unsupported data type")


def make_xml(data: dict | list):
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + __next_object(data)

