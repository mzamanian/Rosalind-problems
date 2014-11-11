#!/bin/python

from sys import argv 
script, filename = argv 

f = open(filename)

Seqs = []
for line in f:
	line = line.strip()
	Seqs.append(line)

Seq1 = Seqs[0]
Seq2 = Seqs[1]

mut_count = 0

for i in range(0,len(Seq1)):
	if Seq1[i] != Seq2[i]:
		mut_count = mut_count + 1
	else:
		mut_count = mut_count
		
print mut_count



