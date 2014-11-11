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

SeqIDs = []
headers = re.findall('>(.*?)%', fstring)
for SeqID in headers:
	SeqIDs.append(SeqID)

Seqs = []
nheaders = re.findall('%([^>]+)%', fstring)  #or [ATGCN]
for Seq in nheaders:
	Seqs.append(Seq)

#initialize profile matrix
length = len(Seqs[0])
A = [0]*length
C = [0]*length
G = [0]*length
T = [0]*length

k = 0
for i in Seqs:
	for j in i:
		if j == 'A':
			A[k] += 1
		elif j == 'C':
			C[k] += 1
		elif j == 'G':			
			G[k] += 1
		elif j == 'T':			
			T[k] += 1
		else:
			pass
		k = k+1
	k = 0

consensus = []
for z in range(length):
	ACGT = [A[z],C[z],G[z],T[z]]
	if A[z] == max(ACGT):
		consensus.append('A'),
	elif C[z] == max(ACGT):
		consensus.append('C'),
	elif G[z] == max(ACGT):
		consensus.append('G'),	
	elif T[z] == max(ACGT):
		consensus.append('T'),
	else:
		pass

print ''.join(consensus)

print 'A:', ' '.join(str(x) for x in A)
print 'C:', ' '.join(str(x) for x in C)
print 'G:', ' '.join(str(x) for x in G)
print 'T:', ' '.join(str(x) for x in T)

f.close()
