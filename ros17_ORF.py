#!/bin/python

import collections
from collections import Counter
from sys import argv 
script, filename = argv 
import re

f = open(filename) 

codon_conversion = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L", "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*", "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M", "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def translate(string):
	codons = []
	triplets = re.findall('([ATGC]{3})',string)
	for codon in triplets:
		codons.append(codon)
	aas = []
	for i in codons:
		aa = codon_conversion[i]
		aas.append(aa)
	peptide = ''.join(aas)
	return peptide

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

def findORFs(string):
	ORFs = []
	for i in range(0,len(string)):
		temp_string = string[i::]
		print temp_string
		hit = re.match('(M.*?)\*',temp_string)
		if hit:
			ORFs.append(hit.group(1))
		else:
			pass
	return ORFs

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

for sequence in Seqs:
	aa_f1 = translate(sequence)
	f1 = findORFs(aa_f1)
	aa_f2 = translate(sequence[1::])
	f2 = findORFs(aa_f2)
	aa_f3 = translate(sequence[2::])
	f3 = findORFs(aa_f3)

	sequence_rc = revcom(sequence)
	aa_r1 = translate(sequence_rc)
	r1 = findORFs(aa_r1)
	aa_r2 = translate(sequence_rc[1::])
	r2 = findORFs(aa_r2)
	aa_r3 = translate(sequence_rc[2::])
	r3 = findORFs(aa_r3)
	
	all_ORFs = f1 + f2 + f3 + r1 + r2 + r3
	all_ORFs = list(set(all_ORFs))
	print '\n'.join(all_ORFs)
f.close()
