#!/bin/python

from sys import argv 
script, k, m, n = argv 

k = float(k)
m = float(m)
n = float(n)
t = k + m + n

prec = 1 - ((n**2) - n + (m * n) + (0.25 * m**2) - (0.25 * m)) / ((t**2) - t)
print prec


# k = homozygous dominant
# m = heterozygous
# n = homozygous recessive
#probability of at least one dominant allele = 1 - probability of homozygous recessive
#odds of homozygous recessive: sum[P(nn)*1,P(mn)*(1/2),P(nm)*(1/2),P(mm)*(1/4)]
#P(nn) = (n/t)*((n-1)/(t-1))
#P(mn) = (m/t)*(n/(t-1)) * 1/2
#P(nm) = (n/t)*(m/(t-1)) * 1/2
#P(mm) = (m/t)*((m-1)/(t-1)) * 1/4
