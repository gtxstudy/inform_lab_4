import re


def parse_yaml(yaml: str):
    return __parse_objects(yaml)[0]


def __parse_objects(yaml: str, pos: int = 0):
    result = {}
    next_pos = __skip_spaces(pos, yaml)
    level = next_pos - pos
    new_level = level
    if yaml[next_pos] == "-":
        result = __parse_list(next_pos, level, yaml)
        return result
    while level == new_level and pos < len(yaml):
        pos = next_pos
        key, key_end = __extract_key(pos, yaml)
        pos = __skip_spaces(key_end + 1, yaml)
        is_obj_simple = not yaml[pos] == "\n"
        if is_obj_simple:
            result[key], pos = __parse_simple(pos, yaml)
        else:
            result[key], pos = __parse_objects(yaml, pos + 1)
        next_pos = __skip_spaces(pos, yaml)
        new_level = next_pos - pos
    return result, pos


def __parse_list(pos: int, level: int, yaml: str):
    result = []
    new_level = level
    if yaml[pos:pos+2] != "- ":
        raise Exception("not a list")
    next_pos = pos
    while level == new_level:
        pos = next_pos
        pos = __skip_spaces(pos + 1, yaml)
        el_end = pos
        while el_end < len(yaml) and not yaml[el_end] == "\n":
            el_end += 1
        element = yaml[pos:el_end]
        pos = __skip_spaces(el_end, yaml)
        if element[-1] == ":":
            is_obj_simple = not yaml[pos] == "\n"
            if is_obj_simple:
                val, pos = __parse_simple(pos, yaml)
            else:
                val, pos = __parse_objects(yaml, pos + 1)
            result.append({element[0:-1]: val})
        else:
            result.append(element)
            pos = el_end
            pos = __skip_spaces(pos, yaml) + 1
        next_pos = __skip_spaces(pos, yaml)
        new_level = next_pos - pos
    return result, pos


def __extract_key(pos: int, yaml: str):
    m = re.match(r"\b[^:]*\b", yaml[pos::])
    return m.group(0), pos+m.end(0)


# \b(\".*\")|(\w*)\b
def __parse_simple(pos: int, yaml: str):
    m = re.match(r"(\"[^\"]*\")|\b(.*)\b", yaml[pos::])
    return m.group(0), m.end(0)+pos+1


def __skip_spaces(start_pos: int, text: str):
    m = re.match(r" *",  text[start_pos::])
    return start_pos+m.end(0)
