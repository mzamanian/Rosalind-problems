#!/bin/python

DNA = raw_input("> Enter Sequence ")
DNAb = list(DNA)
RNAb = []

for base in DNAb:
	if base == 'A':
		RNAb.append('A')
	elif base == 'C':
		RNAb.append('C')
	elif base == 'G':
		RNAb.append('G')
	elif base == 'T':
		RNAb.append('U')
	else:
		print "non-DNA character in string!"
		exit()

print ''.join(RNAb)
