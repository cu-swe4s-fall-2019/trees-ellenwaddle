'''
1. this script should take parameters that specifies which data struct to use:
    - hash
    - AVL
    - tree
2. take a parameter that specifies teh dataset to use, and how many k/v pairs to
use. There are two files available: randomly sorted k/v pairs, and sorted k/v
pairs. both have 10,000 pairs.

3. times how long it takes to insert itmes in database.

4. times how long it takes to search for subset of keys in database.

5. times how long it takes to search for same number of keys that are NOT in
database.

'''
from avl_tree import avl as Ryan_avl
import avl as avl
from hash-tables-ellenwaddle import hash_tables
from hash-tables-ellenwaddle import hash_functions
import binary_tree as bt
import argparse
import sys
import time

'''
first thing to do is to parse dataset into key/value pairs.
'''


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--struct',
                        type = str,
                        help = 'data structure to use: hash, AVL, or tree',
                        required = True)

    parser.add_argument('--dataset',
                        type = str,
                        help = 'dataset: sorted or random. keys in col1, vals in col2',
                        required = True)

    parser.add_argument('--number_of_keys',
                        type = int,
                        help = 'number of keys/values you want to use',
                        required = False)

    args = parser.parse_args()

    pairs = []

    for l in open(args.dataset):
        pair = l.rstrip().split('\t')
        pairs.append(pair)
        pairs = pairs[0:args.number_of_keys]
    #print(pairs)

        keys = []
        values = []
        for i in pairs:
            '''
            turns keys/values into parallel arrays
            '''
            #print(i)
            p = i[0:1]
            #print(p)
            #key, value = p.split(",")
            key = i[0]
            value = i[1]
            keys.append(key)
            values.append(value)

    t0_insert = time.time()


    if args.struct == 'tree':
        '''insert in all keys / values to an avl tree'''

        #print(keys)
        #print(values)
        root = None
        for k in keys:
            try:
                k = int(k)
                root = bt.insert(root, k)
            except:
                print('your keys are not all numeric')
                raise TypeError
        t1_insert = time.time()
        insert_time = t1_insert - t0_insert
        print('insert time', insert_time)
        '''find all keys / values to an avl tree'''
        t0_search = time.time()

        for i in keys:
            n = bt.search(root, 11)

        t1_search= time.time()
        total_time = t1_search - t0_insert
        print('search time', t1_search-t0_search)
        print('total time', total_time)

    if args.struct == 'AVL':
        tree = avl.avltree()
        '''insert'''
        t0_insert = time.time()
        for k in keys:
            tree.insert(key)
        t1_insert = time.time()
        '''
        search
        '''
        t0_search = time.time()

        for k in keys:
            tree.inorder_traverse()

        t1_search = time.time()
        print('insert time', t1_insert- t0_insert)
        print('search time', t1_search-t0_search)
        print('total time', t1_search - t0_insert)

    if args.struct == 'hash':
        ht = hash_tables
        #key = 20
        #sum = 101*2 + 108*2 + 110  # ascii sum of 'ellen'
        #loc = sum % key
        t0_insert = time.time()
        for k in keys:
            ht.add(k)
        t0_insert = time.time()

        t0_search = time.time()
        for k in keys:
            ht.search(k)
        t1_search = time.time()

        print('insert time', t1_insert- t0_insert)
        print('search time', t1_search-t0_search)
        print('total time', t1_search - t0_insert)

# python insert_key_value_pairs.py --struct tree --dataset small_database.txt --number_of_keys 10
# python insert_key_value_pairs.py --struct tree --dataset rand.txt --number_of_keys 1000
# python insert_key_value_pairs.py --struct AVL --dataset random_vals_no_repeats.txt --number_of_keys 1000
# python insert_key_value_pairs.py --struct hash --dataset random_vals_no_repeats.txt --number_of_keys 1000
