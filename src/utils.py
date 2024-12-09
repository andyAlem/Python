import json
from json import JSONDecodeError

def get_transactions(path):
    try:
        with open(path, encoding='utf-8') as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError:
                print('Error')
                return []
        return data_json
    except FileNotFoundError:
        print('File not found')
        return []