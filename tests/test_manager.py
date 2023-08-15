import unittest
from unittest import TestCase
from file import read_dataset, write_dataset
from helper import print_commands,print_result,read_values,print_all_values,keys,values
from manager import create, update, delete,restore_deleted_values
from search import search_record
from main import main
from unittest.mock import patch
class CreateNewUser(TestCase):

    def setUp(self) -> None:
        self.filepath = 'database_test.json'
        self.phone = '380998526455'
        self.dataset = read_dataset(self.filepath)
        self.user_data = ['John', 'Smith', 'LA', 'USA']

    def test_create_new_user(self,):
            input_list = [self.phone, 'John', 'Smith', 'LA', 'USA']
            inputs = iter(input_list)
            with patch("builtins.input", side_effect=inputs):
                data = read_values()
                self.dataset = create(self.dataset, data)
            print(self.dataset)

    def test_update_user_first_name(self):
        pass



    # def tearDown(self) -> None:
    #     write_dataset(self.dataset, self.filepath)
if __name__ == "__main__":
    unittest.main()





