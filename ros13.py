#!/bin/python

import collections
from collections import Counter
from sys import argv 
script, filename = argv 
import re

f = open(filename) 

def checkmatch(seed):
	nh = 0
	for i in Seqs:
		hit = re.search(seed,i)
		if hit:
			nh += 1
		else:
			pass
	return nh

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

seq1 = Seqs[0]  #use seq1 for seeding
num_seqs = len(Seqs) #total # of sequences
seq_length = len(seq1) #length of sequence 1 (= maximum common substring of any sequence)

max_len = 0 
max_sub = ''
for k in range(0,seq_length):
	seq1t = seq1[k:]
	print 'Seq1t:', seq1t
	for i in range(1,seq_length - k + 1):
		temp_string = seq1t[:i]
		temp_len = len(temp_string)
		result = checkmatch(temp_string)
		#print 'TempSeq1:', temp_string, 'templength:', temp_len,'result:',result
		if result == num_seqs:
			if temp_len > max_len:
				max_len = temp_len
				max_sub = temp_string
			else:
				pass
		else:
			break

#print max_len
print max_sub
f.close()
