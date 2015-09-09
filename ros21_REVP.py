#!/bin/python

import collections
from collections import Counter
from sys import argv 
script, filename = argv 
import re

f = open(filename) 

def revcom(string):
	string_r = list(string)
	string_r = string_r[::-1]
	revcom = []
	for base in string_r:
		if base == 'A':
			revcom.append('T')
		elif base == 'C':
			revcom.append('G')
		elif base == 'G':
			revcom.append('C')
		elif base == 'T':
			revcom.append('A')
		else:
			pass
  	rev_com = ''.join(revcom)
  	return rev_com


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

for i in range(4,13): #check subseqs 4-12 in length
	for sequence in Seqs:
		length = len(sequence)
		for b in range(1,length - i + 2): #start at every base, b, 1 -> length - i
			test_seq = sequence[b-1:b+i-1]
			rc_test_seq = revcom(test_seq)
			if test_seq == rc_test_seq:
				print b, i
		

