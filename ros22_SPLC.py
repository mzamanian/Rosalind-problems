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

DNA = Seqs[0]
introns = Seqs[1:]

CDS = DNA
for i in introns:
	CDS = str.replace(CDS, i, "")
print translate(CDS)


