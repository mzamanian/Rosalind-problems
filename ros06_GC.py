#!/bin/python

import collections
from collections import Counter
from sys import argv 
script, filename = argv 
import re

f = open(filename) 

fstring = ''
for line in f:
	line = line.strip()
	header = re.match('^>',line)
	if header:
		fstring = fstring + '%' + line + '%'
	else:
		fstring = fstring + line
fstring = fstring + '%'
print fstring

SeqIDs = []
headers = re.findall('>(.*?)%', fstring)
for SeqID in headers:
	SeqIDs.append(SeqID)

Seqs = []
nheaders = re.findall('%([^>]+)%', fstring)  #or [ATGCN]
for Seq in nheaders:
	Seqs.append(Seq)

j = 0
for i in Seqs:
	print SeqIDs[j]
	c = collections.Counter(i)
	CG = float(c['C'] + c['G'])
	pCG = 100*float(CG/len(i))
	print pCG
	j = j+1

f.close()


