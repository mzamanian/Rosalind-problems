#!/bin/python

import collections
from collections import Counter
from sys import argv 
script, filename = argv 
import re
import math
import itertools

f = open(filename)

alphabet = ''
num = ''
for line in f:
	line = line.strip()
	line = re.sub('\s', '', line)
	digit = re.match('^\d',line)
	if digit:
		num = line
	else:
		alphabet = alphabet + line

alpha = list(alphabet)
num = int(num)
#alpha: list of ordered alphabet
#num: string length

def perm(n, seq):
    for p in itertools.product(seq, repeat=n):
        print "".join(p)

perm(num, alpha)
#print perm