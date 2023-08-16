import unittest
from unittest import TestCase
from file import read_dataset, write_dataset
from helper import print_commands,print_result,read_values,print_all_values,keys,values
from manager import create, update, delete,restore_deleted_values
from search import search_record
from main import main
from unittest.mock import patch
class CreateUpdateDeleteUser(TestCase):

    def setUp(self) -> None:
        self.filepath = 'database_test.json'
        self.phone1 = '380998526455'
        self.phone2 = '380637786375'
        self.dataset = read_dataset(self.filepath)
        self.user_data = ['John', 'Smith', 'LA', 'USA']
        self.user_data2 = ['Lucy', 'Jackson', 'LA', 'USA']

    def test_create_new_user(self):
        input_list = [self.phone1, 'John', 'Smith', 'LA', 'USA']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            data = read_values()
            self.dataset = create(self.dataset, data)
        userdata_in_dataset = ([self.dataset[self.phone1]['first_name'], self.dataset[self.phone1]['last_name'],
                                self.dataset[self.phone1]['city'], self.dataset[self.phone1]['country']])
        self.assertEqual(*self.dataset.keys(), self.phone1)
        self.assertSequenceEqual(self.user_data, userdata_in_dataset)

    def test_update_user_first_name(self):
        new_fname = 'Jack'
        input_list = [self.phone1, new_fname, '', '', '']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone1]['first_name'], new_fname)

    def test_update_user_last_name(self):
        new_lname = 'King'
        input_list = [self.phone1, '', new_lname, '', '']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone1]['last_name'], new_lname)

    def test_update_user_city(self):
        new_city = 'Monreal'
        input_list = [self.phone1, '', '', new_city, '']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone1]['city'], new_city)


    def test_update_user_country(self):
        new_country = 'Canada'
        input_list = [self.phone1, '', '', '', new_country]
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone1]['country'], new_country)


    def test_fail_update_with_incorrect_number(self):
        new_fname = 'Luke'
        phone = '111235'
        input_list = [phone, new_fname, '', '', '']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            err = update(self.dataset)
        self.assertEqual(err, 'Номер відстуній в книжці')

    def create_second_user(self):
        input_list = [self.phone2, 'Lucy', 'Jackson', 'LA', 'USA']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            data = read_values()
            create(self.dataset, data)

    def test_delete_user(self):
        self.create_second_user()
        with patch("builtins.input", return_value=self.phone2):
            delete(self.dataset)

    def tearDown(self) -> None:
        write_dataset(self.dataset, self.filepath)


class SearchUser(TestCase):

    def setUp(self) -> None:
        self.filepath = 'database_test.json'
        self.phone = '380998526455'
        self.phone2 = '380637786375'
        self.dataset = read_dataset(self.filepath)
        self.first_name = self.dataset[self.phone]['first_name']
        self.last_name = self.dataset[self.phone]['last_name']
        self.city = self.dataset[self.phone]['city']
        self.country = self.dataset[self.phone]['country']

    def test_search_by_first_name(self):
        command = 'sf'
        with patch("builtins.input", return_value=self.first_name):
            result = search_record(self.dataset, command, self.first_name)
            self.assertEqual(self.phone, *result.keys())
            self.assertEqual(self.first_name, result[self.phone]['first_name'])

    def test_search_by_name_not_from_dataset(self):
        command = 'sf'
        fname = 'Jill'
        with patch("builtins.input", return_value=fname):
            result = search_record(self.dataset, command, fname)
        self.assertEqual(result, {})

    def test_search_by_last_name(self):
        command = 'sl'
        with patch("builtins.input", return_value=self.last_name):
            result = search_record(self.dataset, command, self.last_name)
            self.assertEqual(self.phone, *result.keys())
            self.assertEqual(self.last_name, result[self.phone]['last_name'])

    def test_search_by_first_and_last_name(self):
        command = 'sfl'
        input_list = [self.first_name, self.last_name]
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            result = search_record(self.dataset, command, (self.first_name + ' ' + self.last_name).split(' '))
            self.assertEqual(self.phone, *result.keys())
            self.assertEqual(self.last_name, result[self.phone]['last_name'])
            self.assertEqual(self.first_name,result[self.phone]['first_name'])

    def test_search_by_phone(self):
        command = 'sp'
        with patch("builtins.input", return_value=self.phone):
            result = search_record(self.dataset, command, self.phone)
            self.assertEqual(self.phone, *result.keys())

    def test_search_by_city(self):
        command = 'sct'
        with patch("builtins.input", return_value=self.city):
            result = search_record(self.dataset, command, self.city)
            self.assertEqual(self.phone, *result.keys())
            self.assertEqual(self.city, result[self.phone]['city'])

    def test_search_by_country(self):
        command = 'sc'
        with patch("builtins.input", return_value=self.country):
            result = search_record(self.dataset, command, self.country)
            self.assertEqual(self.phone, *result.keys())
            self.assertEqual(self.country, result[self.phone]['country'])




if __name__ == "__main__":
    unittest.main()





