import json

def read_dataset(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_dataset(dataset, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(dataset, file)


if __name__ == '__main__':
    filepath = 'database/database.json'
    print(read_dataset(filepath))
    # dataset = {"+380638362628": {"phone_number": "Olya", "first_name": "Semenova", "city": "Kyiv", "country": "UKRAINE"}}