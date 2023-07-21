from file import read_dataset, write_dataset
from helper import print_commands, print_result, read_values, keys, values
from manager import create, update, delete
from search import search_record


def main(file_path):
    print_commands()
    dataset = read_dataset(file_path)
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
            pass
        elif command == 'sfl':
            pass
        elif command == 'sp':
            value = input('Введіть номер телефону: ')
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == 'sct':
            pass
        elif command == 'sc':
            pass
        elif command == 'up':
            update(dataset)
        elif command == 'del':
            delete(dataset)
        elif command == 'help':
            print_commands()
        elif command == 'exit':
            write_dataset(dataset, file_path)
            break
        else:
            print('Дана команда недоступна')


if __name__ == '__main__':
    main('database/database.json')