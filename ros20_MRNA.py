#!/bin/python

import collections
from collections import Counter
from sys import argv 
script, aa_seq = argv 
import re

codon_nums = {"I" : 3, "L" : 6, "V" : 4, "F" : 2, "M" : 1, "C" : 2, "A" : 4, "G" : 4, "P" : 4, "T" : 4, "S" : 6, "Y" : 2, "W" : 1, "Q" : 2, "N" : 2, "H" : 2, "E" : 2, "D" : 2, "K" : 2, "R" : 6, "*" : 3}

def nums(string):
	counts = []
	AAs = re.findall('([A-Z|*]{1})',string)
	for aa in AAs:
		counts.append(codon_nums[aa])
	j = 1
	for i in counts:
		j = (j * i) % 1000000
	return j*3 % 1000000

print nums(aa_seq)
