from file import read_dataset

base_dict = {
    'phone_number': {
        'first_name': '',
        'last_name': '',
        'city': '',
        'country': '',
    }
} #dataset example structure

keys = ['first_name', 'last_name', 'city', 'country']
values = ['ім\'я', 'прізвище', 'місто', 'країна']

def print_commands():
    print('Доступні команди:',
          'new - створити новий запис',
          'sf - пошук за ім\'ям',
          'sl - пошук за прізвищем',
          'sfl - пошук за повним іменем',
          'sp - пошук за телефоном',
          'sсt - пошук за містом',
          'sс - пошук за країною',
          'up - оновлення запису',
          'del - видалення запису',
          'rdv - відновлення видалених записів',
          'printall - виведення всіх записів у книжці',
          'help - список команд',
          'exit - вихід з програми', sep='\n')

def print_result(result):
    for phone, data in result.items():
        print('Номер телефону', phone)
        for name, record in zip(values, data):
            print(f'\t{name.capitalize()}: {data[record]}')


def read_values():
    phone = input('Введіть номер: ')
    new_data = {phone: {}}
    for key, value in zip(keys, values):
        if value == 'країна' :
            value = 'країну'
        new_data[phone][key] = input(f'Введіть {value}: ')
    return new_data


def print_all_values(dataset):
    print_result(dataset)


# filepath ='database/database.json'
# dataset = read_dataset(filepath)
# print_all_values(dataset)
# print_commands()

# print(read_values())

# print_result(result)

