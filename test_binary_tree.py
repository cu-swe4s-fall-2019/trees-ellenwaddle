import unittest
import binary_tree as bt
import random

'''unit testing for binary trees'''

class TestBinaryTrees(unittest.TestCase):
    def test_key_is_inserted_root_is_none(self):
        root = None
        root = bt.insert(root, 11, 1)
        self.assertEqual(root.value, 1)

    def test_insert_actually_inserts_on_correct_side(self):
        root = None
        root = bt.insert(root, 11, 1)
        root = bt.insert(root, 5, 5)
        self.assertEqual(root.left.value, 5)

    def test_can_search(self):
        root = None
        root = bt.insert(root, 11, 1)
        root = bt.insert(root, 5, 6)
        root = bt.insert(root, 42, 21)
        s = bt.search(root, 5)
        self.assertEqual(s.value, 6)

    def test_key_is_string(self):

        root = None
        result = bt.insert(root, 'ellen', 12)
        self.assertEqual(result, 'your key should be numeric, not a string')

    def test_search_cannot_find_value(self):
        root = None
        root = bt.insert(root, 102, 129)
        s = bt.search(root, 1000)
        self.assertEqual(s, 'key not found')

if __name__ == '__main__':
    unittest.main()
