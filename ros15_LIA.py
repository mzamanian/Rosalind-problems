#!/bin/python

import math
from sys import argv 
script, k, N = argv 

k = int(k)
N = int(N)

def nCr(a,b):
    f = math.factorial
    return f(a) / f(b) / f(a-b)

sum = 0
for i in range(N,(2**k)+1):
	print i
	temp = nCr(2**k,i)*(0.25**(i))*(0.75**((2**k)-i))
	sum = sum + temp
print float(sum)