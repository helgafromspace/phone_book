from unittest import TestCase
from file import read_dataset, write_dataset
from helper import print_commands,print_result,read_values,print_all_values,keys,values
from manager import create, update, delete,restore_deleted_values
from search import search_record
from main import main

class CreateNewUser(TestCase):
    def setUp(self) -> None:
        self.filepath = 'database_test.json'
        self.dataset = read_dataset(self.filepath)
        self.phone_1 = '380998526455'
        self.user_1_data = ['John', 'Smith', 'LA', '']

    def test_read_dataset(self):
        self.dataset = read_dataset(self.filepath)
        self.assertEqual(self.dataset, {})

    def test_create_new_user(self):
        new_data = {self.phone_1: {}}
        for key, user_data in zip(keys, self.user_1_data):
            new_data[self.phone_1][key] = user_data
        self.dataset = create(self.dataset, new_data)
        self.assertEqual(self.phone_1, *self.dataset.keys())
        user_data_in_dataset = ([self.dataset[self.phone_1]['first_name'], self.dataset[self.phone_1]['last_name'],
                                 self.dataset[self.phone_1]['city'], self.dataset[self.phone_1]['country']])
        self.assertSequenceEqual(self.user_1_data, user_data_in_dataset)





