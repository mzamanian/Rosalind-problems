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

#probability of at least one dominant allele = 1 - probability of homozygous recessive
#odds of homozygous recessive: sum[P(nn)*1,P(mn)*(1/2),P(nm)*(1/2),P(mm)*(1/4)]
#P(nn) = (n/t)*((n-1)/(t-1))
#P(mn) = (m/t)*(n/(t-1)) * 1/2
#P(nm) = (n/t)*(m/(t-1)) * 1/2
#P(mm) = (m/t)*((m-1)/(t-1)) * 1/4
#P(recessive) = ((n**2) - n + (m*n*0.5) / ((t**2) - t)
