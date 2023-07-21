base_dict = {
    'phone_number': {
        'first_name': '',
        'last_name': '',
        'city': '',
        'country': '',
    }
} #dataset example structure

keys = ['first_name', 'last_name', 'city', 'country']
values = ['ім\'я', 'прізвище', 'місто', 'країнy']

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
        new_data[phone][key] = input(f'Введіть {value}: ')
    return new_data


# result = {
#     '+380638362628': {
#         'first_name': 'Olya',
#         'last_name': 'Semenova',
#         'city': 'Kyiv',
#         'country': 'Ukraine',
#     }
# }

# print_commands()

# print(read_values())

# print_result(result)

