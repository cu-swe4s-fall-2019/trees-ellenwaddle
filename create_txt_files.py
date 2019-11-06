#create random and sorted key files
import random
import sys

r = []
for i in range(0,10000):
    x = str(random.randint(1,10000))
    r.append(x)
rfile = open('random_vals.txt', 'w')
for i in r:
    rfile.write(i + "\n")
rfile.close()

#if __name__ == '__main__':
