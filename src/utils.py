import json
from json import JSONDecodeError

def get_transactions(path):
    """Функция принимает на вход путь до JSON-файла
     и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='utf-8') as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError:
                print('Error decoding')
                return []
        return data_json
    except FileNotFoundError:
        print('File not found')
        return []