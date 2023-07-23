from file import read_dataset, write_dataset
from helper import print_commands, print_result, read_values, print_all_values
from manager import create, update, delete,restore_deleted_values
from search import search_record


def main(file_path):
    dataset = read_dataset(file_path)
    print_commands()
    while True:
        command = input('Введіть команду зі списку: ')
        if command == 'new':
            values = read_values()
            dataset = create(dataset, values)
        elif command == 'sf':
            value = input('Введіть ім\'я: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sl':
            value = input('Введіть прізвище: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sfl':
            value = input('Введіть ім\'я: ') + ' ' + input('Введіть прізвище: ')
            value = value.split(' ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sp':
            value = input('Введіть номер телефону: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sct':
            value = input('Введіть місто: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sc':
            value = input('Введіть країну: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'up':
            update(dataset)
        elif command == 'del':
            delete(dataset)
        elif command == 'rdv':
            restore_deleted_values(dataset)
            print('Deleted values from current session are restored')
        elif command == 'printall':
            print_all_values(dataset)
        elif command == 'help':
            print_commands()
        elif command == 'exit':
            write_dataset(dataset, file_path)
            break
        else:
            print('Дана команда недоступна')


if __name__ == '__main__':
    filepath = 'database/database.json'
    try:
        main(filepath)
    except FileNotFoundError:
        print('File not found. Please, check filepath validity')