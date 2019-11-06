class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


    def insert(root, key, value=None):
        '''
        function to insert a key, value pair into trees
        '''
        if self.key is None:
            self.key = key
            self.value = value
        elif key > self.key:
            insert(self.right, key, value)
        elif key < self.key:
            insert(self.left, key, value)
        else:
            return 'insertion failed: is your key numeric?'


    def search(root, key):
        '''
        function to search keys in a tree
        '''
        if self.key == key:
            return self.value
        elif key < self.key:
            search(self.left, key)
        elif key > self.key:
            search(self.right, key)
        else:
            return -1

if __name__ == '__main__':
    Node()
