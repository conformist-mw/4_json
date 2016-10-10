import json
import argparse


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f, encoding='utf-8')
    return data


def pretty_print_json(data):
    return json.dumps(data, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Выводит содержимое файла json в удобном формате')
    parser.add_argument('filepath', help='укажите файл в формате json')
    args = parser.parse_args()
    data = load_data(args.filepath)
    print(pretty_print_json(data))
