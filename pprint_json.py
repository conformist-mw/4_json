import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f, encoding='utf-8')
    return data


def pretty_print_json(data):
    return json.dumps(data, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    print(pretty_print_json(data))
