#!/bin/python

DNA = raw_input("> Enter Sequence ")
DNAb = list(DNA)
DNAr = DNAb[::-1]
DNAc = []

for base in DNAr:
	if base == 'A':
		DNAc.append('T')
	elif base == 'C':
		DNAc.append('G')
	elif base == 'G':
		DNAc.append('C')
	elif base == 'T':
		DNAc.append('A')
	else:
		print "non-DNA character in string!"
		exit()

print ''.join(DNAc)