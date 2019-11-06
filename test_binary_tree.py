import unittest
import binary_tree as bt


'''unit testing for binary trees'''

class TestBinaryTrees(unittest.TestCase):
    def test_key_is_string(self):
        result = bt.insert(12, 'ellen')
        self.assertEqual(result, 'insertion failed: is your key numeric?')

    def test_insert_actually_inserts(self):
        root = 10
        key = 5
        value = 5
        result = bt.insert(root, key, value)
        self.assertNotEqual(result, 'insertion failed: is your key numeric?')

    def test_search_finds_inserted_value(self):
        root = 10
        key = 5
        value = 5
        insert = bt.insert(root, key, value)
        s = bt.search(root, key)
        self.assertNotEqual(s, -1)

if __name__ == '__main__':
    unittest.main()
