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
nheaders = re.findall('%([^>]+)%', fstring) 
for Seq in nheaders:
	Seqs.append(Seq)

num_seqs = len(Seqs)
k = 3

for i in range (0,num_seqs):
	curr_seq = Seqs[i]
	seq_len = len(curr_seq)

	for j in range (i+1,num_seqs):
		test_seq = Seqs[j]
		tseq_len = len(test_seq)
		hit_begin = re.match(curr_seq[0:k],test_seq[tseq_len-k:])
		if hit_begin and curr_seq != test_seq :
			print SeqIDs[j], SeqIDs[i]
		else:
			pass
		
		hit_end = re.match(curr_seq[seq_len-k:seq_len],test_seq[0:k])
		if hit_end and curr_seq != test_seq:
			print SeqIDs[i], SeqIDs[j]
		else:
			pass

f.close()
