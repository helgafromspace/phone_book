def search_record(dataset, search_type, value):  # value - is part or full number (1)
    result = {}
    if search_type == 'sp':
        for phone in dataset:
            if value in phone:
                result.update({phone: dataset[phone]})
    elif search_type == 'sf':
        for phone, data in dataset.items():
            if value in data['first_name']:
                result.update({phone: dataset[phone]})
    return result