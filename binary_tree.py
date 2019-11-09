class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value=None):
    try:
        float(key)
        if root is None:
            root = Node(key, value=value)
            return root
        else:
            if key < root.key:
                if root.left is None:
                    root.left = Node(key, value=value)
                else:
                    insert(root.left, key, value=value)
            else:
                if root.right is None:
                    root.right = Node(key, value=value)
                else:
                    insert(root.right, key, value=value)
            return root
    except:
        return('your key should be numeric, not a string')


def search(root, key):
        '''
        function to search keys in a tree. will return a value associatied w
        that key
        '''
        if root is None:
            return root

        elif root.key == key:
            return root

        elif key > root.key:
            if root.right is None:
                return 'key not found'
            else:
                return search(root.right, key)

        elif key < root.key:
            if root.left is None:
                return 'key not found'
            else:
                return search(root.left, key)

if __name__ == '__main__':
    '''
    practicing with some insertions and searches
    '''
    root = None
    root = insert(root, 10, 40)
    root = insert(root, 9, 1)
    #print('root.key', root.key)
    #print('root.value', root.value )
    root = insert(root, 15, 1)
    root = insert(root, 11, 4)
    n = search(root, 11)
    print(n.value)

    #print(root.key, root.value)
    #print(root.left.key, root.left.value)
    #print(root.right.left.key)
