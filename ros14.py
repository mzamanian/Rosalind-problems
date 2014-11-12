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
		hit_begin = re.match(curr_seq[0:k],test_seq[tseq_len-k:]) #match beginning to end
		if hit_begin and curr_seq != test_seq :
			print SeqIDs[j], SeqIDs[i]
			#print Seqs[j], Seqs[i]
			#print 'curr_beg:', curr_seq[0:k], 'test_end:', test_seq[tseq_len-k:], "\n"
		else:
			pass
		
		hit_end = re.match(curr_seq[seq_len-k:seq_len],test_seq[0:k]) #match end to beginning
		if hit_end and curr_seq != test_seq:
			print SeqIDs[i], SeqIDs[j]
			#print Seqs[i], Seqs[j]
			#print 'curr_end:', curr_seq[seq_len-k:seq_len], 'test_begin:', test_seq[0:k], "\n"
		else:
			pass



f.close()
