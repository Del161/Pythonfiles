#!/usr/bin/env python 
import sys

arguments = sys.argv
#argument index 1 is input bestandsnaam, index 2 output bestandsnaam, index 3 reading frame

if len(arguments) < 3:
    print("insufficient arguments!")
else: inputnaam = "./Fasta-Sequence/" + arguments[1]
if len(arguments) < 3:
    print("insufficient arguments!")
else: outputnaam = "./Fasta-Sequence/" + arguments[2]

if len(arguments) < 4:
    reading_frame = 0
else: reading_frame = int(arguments[3]) - 1

proteins_end = []
proteins = []
codontabel = {
    # 'M' - START, '*' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "*", "TAG": "*", "TGA": "*"
    #bron codontabel https://rebelscience.club/2020/04/dna-toolkit-part-4-translation-codon-usage/
}

#opent bestand en haalt informatie eruit.
with open(inputnaam, "r") as file:
    dna_codons = []
    seq = file.readlines()
    seq = "".join(seq[1:len(seq)])
    seq = seq.replace("\n","")


#check reading frame correct, en voeg codons toe
    if reading_frame > -1 and reading_frame < 3:
        for char in range(reading_frame, len(seq), 3):
            dna_codons.append(seq[char:char + 3])
    else: print("Reading frame has to be 1 2 or 3!")

#check of codon lang genoeg is, zowel print dan bijpassende protein
for codons in dna_codons:
    if len(codons) < 3:
        print("laatste codon is te kort voor enzym: ", codons)
    else: 
        proteins.append(codontabel[codons]) 

#maak regels van 70
for aantal_p in range(0,len(proteins),70):
    proteins_end.append("".join(proteins[aantal_p: aantal_p + 70]))

#schrijft de output in een bestand
with open(outputnaam,"w") as writefile:
    writefile.write(">NG_005905.2 Homo sapiens BRCA1 DNA repair associated (BRCA1), RefSeqGene (LRG_292) on chromosome 17 \n")
    for regels in proteins_end:
        writefile.write(regels)
        writefile.write("\n") 