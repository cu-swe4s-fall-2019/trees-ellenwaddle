'''
writing my 'own' AVL tree. code mostly taken from:
https://blog.coder.si/2014/02/how-to-implement-avl-tree-in-python.html
'''


class Node:
    '''
    AVL tree node class
    '''
    def __init__(self, key):
        '''
        make nodes
        '''
        "Construct."

        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        "String representation."
        return str(self.key)

    def __repr__(self):
        "String representation."
        return str(self.key)


class avltree(object):
    '''
    an avl tree
    '''
    def __init__(self):
        "Construct."

        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, key):
        '''
        insert new key
        '''
        n = Node(key)

        if not self.node:
            self.node = n
            self.node.left = avltree()
            self.node.right = avltree()
        # insert key to left subtree
        elif key < self.node.key:
            self.node.left.insert(key)
        # insert to right
        elif key > self.node.key:
            self.node.right.insert(key)

        # no duplicates allowed, exit if key exists already

        # rebalance if needed
        self.rebalance()

    def rebalance(self):
        '''
        to check if we need to rebalance, update heights
        '''
        self.update_heights(recursive=False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:  # left subtree larger than right
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:  # right larger than left
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        '''
        update tree heights. h is max of right or left distance from leaf to
        node
        '''
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            max_height = max(self.node.left.height, self.node.right.height)
            self.height = 1 + max_height
        else:
            self.height = -1

    def update_balances(self, recursive=True):
        '''
        calculate tree balance factor:
        balance = height(left subtree) - h(right subtree)
        '''

        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

                self.balance = self.node.left.height - self.node.right.height
            else:
                self.balance = 0

    def rotate_right(self):
        '''
        right rotation. change self to right subtree of left
        '''
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        '''
        left rotation. set self to left subtree of right
        '''
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def delete(self, key):
        '''
        delete a key from the tree. f tree only has left or right subree,
        it's replaced with one of them.
        In worst case scenario, tree has both left and right subtrees.
        In this case we need to find logical successor or predecessor.
        Successor is smalles node in it's right subtree.
        Predecessor is it's largest node in left subtree.
        '''
        if self.node is not None:
            if self.node.key == key:
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                elif not self.node.left.node:
                    self.node = self.node.right.node
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    successor = self.node.right.node
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node.key = successor.key
                        self.node.right.delete(successor.key)

            elif key < self.node.key:
                self.node.left.delete(key)

            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()

    def inorder_traverse(self):
        '''
        inorder traversal of tree
        left subtree + root + right
        '''
        result = []
        if not self.node: # special case for the root
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node.key)
        result.extend(self.node.right.inorder_traverse())

        return result

    def display(self, node=None, level=0):
        if not node:
            node = self.node

        if node.right.node:
            self.display(node.right.node, level + 1)
            print(('\t' * level), ('    /'))

        print(('\t' * level), node)

        if node.left.node:
            print(('\t' * level), ('     \\'))
            self.display(node.left.node, level + 1)


if __name__ == '__main__':
    '''
    Demo
    '''

    tree = avltree()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    data = [10, 9, 8, 7, 6, 12, 14, 15, 16, 20]

    from random import randrange
    for key in data:
        tree.insert(key)

    for key in [4, 3]:
        tree.delete(key)

    to_print = tree.inorder_traverse()
    print(tree.inorder_traverse())
    tree.display()
