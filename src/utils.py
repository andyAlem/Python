import json

def transactions_file(path):
    try:
        with open(path, "r", encoding="utf-8") as date_json:
            return json.load(date_json)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []