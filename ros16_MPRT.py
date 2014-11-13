#!/bin/python

import re
import requests
from sys import argv 
script, filename = argv 

f = open(filename) 

SeqIDs = []
for line in f:
	SeqID = line.strip()
	SeqIDs.append(SeqID)

for seqid in SeqIDs:
	url = 'http://www.uniprot.org/uniprot/' + seqid + '.fasta'
	fasta = requests.get(url)
	fasta.encoding = 'utf-8'

	fasta_str = ''
	for line in fasta:
		line = line.replace(" ", "")
		fasta_str += line
	fasta_str = fasta_str.replace("\n", "")

	AAs = re.search('>.+\d([A-Z]+)',fasta_str)
	seq = AAs.group(1)

	motif = re.compile("N[^P][ST][^P]")

	first_check = motif.search(seq)
	if first_check:
		print seqid
	else:
		pass

	for i in range(0,len(seq)):
		temp_seq = seq[i::]
		hit = motif.match(temp_seq)
		if hit:
			print i + 1,
		else:
			pass

	#non-overlapping hits
	#for m in motif.finditer(seq): 
	#	print m.start() + 1,
	#   print m.group() #for actual hits
	
	if first_check:
		print "\n",
	else:
		pass
