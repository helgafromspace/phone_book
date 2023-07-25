from file import read_dataset


def search_record(dataset, search_type, value):  # value - is part or full number (1)
    result = {}
    count = 0
    if search_type == 'sp':
        for phone in dataset:
            if value in phone:
                count += 1
                result.update({phone: dataset[phone]})
    elif search_type == 'sf':
        for phone, data in dataset.items():
            if data['first_name'].lower().startswith(value.lower()):
                count += 1
                result.update({phone: dataset[phone]})
    elif search_type == 'sl':
        for phone, data in dataset.items():
            if data['last_name'].lower().startswith(value.lower()):
                count += 1
                result.update({phone: dataset[phone]})
    elif search_type == 'sfl':
        for phone, data in dataset.items():
            if data['first_name'].lower().startswith(value[0].lower()) and data['last_name'].lower().startswith(value[1].lower()):
                count += 1
                result.update({phone: dataset[phone]})
    elif search_type == 'sct':
        for phone, data in dataset.items():
            if data['city'].lower().startswith(value.lower()):
                count += 1
                result.update({phone: dataset[phone]})
    elif search_type == 'sc':
        for phone, data in dataset.items():
            if data['country'].lower().startswith(value.lower()):
                count += 1
                result.update({phone: dataset[phone]})
    if count == 0:
        print('Дані відсутні')
    return result

if __name__ == '__main__':
    filepath ='database/database.json'
    dataset = read_dataset(filepath)
    print(dataset)
    # print(search_record(dataset, 'sp', '063'))
    # print(search_record(dataset, 'sf', 'Lu'))
    # print (search_record(dataset, 'sl', 'Sem'))