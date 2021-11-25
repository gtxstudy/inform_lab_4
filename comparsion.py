import yaml
from dict2xml import dict2xml
from time import time

from yaml_parser import parse_yaml
from yaml_parser_with_regex import parse_yaml as parse_yaml_wreg
from xml_maker import make_xml


def parse_and_convert_wlib(data: str):
    parsed = yaml.safe_load(data)
    return dict2xml(parsed)


def parse_and_convert_s(data: str):
    parsed = parse_yaml(data)
    return make_xml(parsed)


def parse_and_convert_wreg(data: str):
    parsed = parse_yaml_wreg(data)
    return make_xml(parsed)


def test(func, data):
    for i in range(10):
        _ = func(data)


if __name__ == "__main__":
    f = open("out/schedule.yaml", "r")
    loaded = f.read()
    f.close()

    st = time()
    test(parse_and_convert_s, loaded)
    d1 = time() - st

    st = time()
    test(parse_and_convert_wreg, loaded)
    d2 = time() - st

    st = time()
    test(parse_and_convert_wlib, loaded)
    d3 = time() - st

    print(f"время способа 1: {d1}\nвремя способа 2: {d2}\nвремя способа 3: {d3}")
