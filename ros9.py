#!/bin/python

from sys import argv 
script, filename = argv 
import re

f = open(filename)

Seqs = []
for line in f:
	line = line.strip()
	Seqs.append(line)

string = Seqs[0]
substr = Seqs[1]

j = len(string) - len(substr)

for i in range (0,j):
	hit = re.match(substr,string)
	if hit:
		print i+1,
	else:
		pass
	temp = list(string)
	del temp[0]
	string = ''.join(temp)

f.close()


