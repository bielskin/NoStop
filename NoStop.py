#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:20:16 2021

@author: NVB
"""

import argparse

parser = argparse.ArgumentParser(description='NOSTOP: Removes stop codons from a codon aligned fasta formatted nucleotide file and replaces with gaps')
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument("-i", "--input_align_file",  help="File of codon aligned nucleotide fasta file", required=True)

args = parser.parse_args()

alignment_file=(vars(args)['input_align_file'])


alignment = {}

file_one= open(alignment_file, 'r')
for line in file_one:
    line = line.strip()
    if not line:
        continue
    if line.startswith(">"):
        active_sequence_name = line[1:]
        if active_sequence_name not in alignment:
            alignment[active_sequence_name] = []
        continue
    sequence = line
    sequence=sequence.replace('TAG-', '---').replace('TGA-', '---').replace('TAA-', '---')
    minusthreeseq=len(sequence)-3
    lastcodon=sequence[minusthreeseq:len(sequence)]

    if lastcodon == "TAA" or lastcodon== "TAG" or lastcodon== "TGA":
            sequence=sequence[0:len(sequence)-3]
            sequence=sequence + '---'
  
            alignment[active_sequence_name]=sequence
    
    else:
            alignment[active_sequence_name]=sequence
    
    
file_one.close()



reduced_alignfile=alignment_file.replace('.fasta', '')

OutFileName=reduced_alignfile + '_NoStop.fasta'
WriteOutFile= True
OutFile=open(OutFileName, 'w')
for seq in alignment:
    OutFile.write(">" + seq + '\n')
    OutFile.write(alignment[seq] +'\n')