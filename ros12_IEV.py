#!/bin/python

from sys import argv 
script, a, b, c, d, e, f = argv 

a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)
f = float(f)
t = a + b + d + e + f

Evalue = 2 * (a + b + c + (0.75 * d) + (0.5 * e))
print Evalue


# probability of at least one dominant allele
# a = AA-AA 1
# b = AA-Aa 1
# c = AA-aa 1
# d = Aa-Aa 0.75
# e = Aa-aa 0.5
# f = aa-aa 0
