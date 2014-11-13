#!/bin/python
import collections
from collections import Counter

#dna = raw_input("> Enter Sequence ")
dna = 'ATGCTATAAAATTT'
dna = dna.strip()

#dnalist = list(dna)


##
c = collections.Counter(dna)   #or in dnalist
print c['A'], '\t', c['C'], '\t', c['G'], '\t', c['T']


### 

c2 = Counter()
for i in dna:  #or in dnalist
	c2[i] += 1
print c2['A'], '\t', c2['C'], '\t', c2['G'], '\t', c2['T']

##

A = 0
C = 0
G = 0
T = 0

for base in dna:  # or in dnalist
	if base == 'A':
		A = A + 1
	elif base == 'C':
		C = C + 1
	elif base == 'G':
		G = G + 1
	elif base == 'T':
		T = T + 1
	else:
		print "non-DNA character in string!"
		exit()
print A, '\t', C, '\t', G, '\t', T, '\n'

##


