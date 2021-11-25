from yaml_parser_with_regex import *
from xml_maker import *

if __name__ == "__main__":
    with open("out/schedule.yaml", "r") as f:
        text = f.read()
        serialized = parse_yaml(text)
        print(serialized)
    with open("out/schedule3.xml", 'w') as fo:
        fo.write(make_xml(serialized))
