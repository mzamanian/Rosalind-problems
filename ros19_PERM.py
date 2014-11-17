#!/bin/python

import math
from sys import argv 
script, n = argv

n = int(n)
print math.factorial(n)

a = range(1,n+1)
print ' '.join(str(x) for x in a)

def perm(n):
    a = range(1, n+1)

    while True:
        m = z = None

        for i in range(0, len(a) - 1):
            if a[i] < a[i+1]:
                m = i

        if m == None:
            break

        for i in range(m + 1, len(a)):
            if a[m] < a[i]:
                z = i

        a[m], a[z] = a[z], a[m]
        a[m+1:] = reversed(a[m+1:])
        yield a[:]
        

for j in perm(n):
	print ' '.join(str(x) for x in j)



