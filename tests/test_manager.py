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
        self.phone = '380998526455'
        self.dataset = read_dataset(self.filepath)
        self.user_data = ['John', 'Smith', 'LA', 'USA']

    def test_create_new_user(self):
        input_list = [self.phone, 'John', 'Smith', 'LA', 'USA']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            data = read_values()
            self.dataset = create(self.dataset, data)
        userdata_in_dataset = ([self.dataset[self.phone]['first_name'], self.dataset[self.phone]['last_name'],
                                self.dataset[self.phone]['city'], self.dataset[self.phone]['country']])
        self.assertEqual(*self.dataset.keys(), self.phone)
        self.assertSequenceEqual(self.user_data, userdata_in_dataset)

    def test_update_user_first_name(self):
        new_fname = 'Jack'
        input_list = [self.phone, new_fname, '', '', '']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone]['first_name'], new_fname)

    def test_update_user_last_name(self):
        new_lname = 'King'
        input_list = [self.phone, '', new_lname, '', '']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone]['last_name'], new_lname)

    def test_update_user_city(self):
        new_city = 'Monreal'
        input_list = [self.phone, '', '', new_city, '']
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone]['city'], new_city)

    def test_update_user_country(self):
        new_country = 'Canada'
        input_list = [self.phone, '', '', '', new_country]
        inputs = iter(input_list)
        with patch("builtins.input", side_effect=inputs):
            update(self.dataset)
        self.assertEqual(self.dataset[self.phone]['country'], new_country)

    def tearDown(self) -> None:
        write_dataset(self.dataset, self.filepath)

if __name__ == "__main__":
    unittest.main()





