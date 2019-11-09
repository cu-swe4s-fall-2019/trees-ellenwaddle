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

#mport hash-tables-ellenwaddle as ht
import avl_tree
import binary_tree as bt
import argparse
import sys


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

    if args.struct == 'tree':
        '''insert in all keys / values to an avl tree'''
        t0_insert = time.time()
        root = None
        keys = []
        values = []
        for i in pairs:
            k = l.rstrip().split()
            keys.append(k[0])
            values.append(k[1])
        print(keys)


        t1_insert = time.time()
        insert_time = t1_insert - t0_insert
        #print(insert_time, ())
        '''find all keys / values to an avl tree'''



# python insert_key_value_pairs.py --struct tree --dataset small_database.txt --number_of_keys 10
