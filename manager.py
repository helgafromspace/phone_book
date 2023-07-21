from helper import read_values, keys, values
def create(dataset: dict, data: dict):
    dataset.update(data)
    return dataset

def update(dataset:dict):
    phone = input('Введіть номер телефону: ')
    if phone in dataset:
        for key, value in zip(keys, values):
            if dataset[phone][key]:
                user_value = input(f'Введіть {value}: ')
                if user_value == '':
                    continue
                else:
                    dataset[phone][key] = user_value
            else:
                user_info = input(f'Бажаєте додати {value}? Напишіть так, якщо потрібно додати, або Enter щоб пропустити\n')
                if user_info == 'так':
                    dataset[phone][key] = input(f'Введіть {value}: ')
                else:
                    continue
    else:
        print('Номер відстуній в книжці')
    return dataset

def delete(dataset):
    phone = input('Введіть номер телефону: ')
    deleted_value = dataset[phone]
    if phone in dataset:
        del dataset[phone]
    else:
        print('Номер відсутній у книжці')
    return dataset


if __name__ == '__main__':
    pass
    # from file import read_dataset, write_dataset
    # user_olya = {
    #     '+380638362628': {
    #         'first_name': 'Olya',
    #         'last_name': 'Semenova',
    #         'city': '',
    #         'country': 'Ukraine',
    #     }
    # }
    # user_sam = {
    #     '+16024567897': {
    #         'first_name': 'Sam',
    #         'last_name': 'Rockwell',
    #         'city': '',
    #         'country': '',
    #     }
    # }
    #
    # filepath ='database/database.json'
    # dataset = read_dataset(filepath)
    # print(dataset)
    # create(dataset, user_olya)
    # create(dataset, user_sam)
    # print(dataset)
    # delete(dataset)
    # print (dataset)
    # # update(dataset)
    # # print(dataset)
    # # write_dataset(dataset, filepath)
