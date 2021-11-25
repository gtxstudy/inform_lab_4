import yaml
from dict2xml import dict2xml

"""
    Почему-то либа по-другому читает массивы, то есть
    заголовок, который стоял перед массивом повторяется много раз,
    оборачивая каждый элемент массива, по-моему это не норм /:
"""

if __name__ == "__main__":
    with open("out/schedule.yaml", "r") as f:
        data = yaml.safe_load(f)
    with open('out/schedule2.xml', 'w') as fo:
        fo.write(dict2xml(data))
