import sys
import gzip
def readFasta(fasta):
    Nucleotidos= {'TTT': 'K', 'TTC': 'K', 'TTA': 'N', 'TTG': 'N', 'TCT': 'R', 'TCC': 'R', 'TCA': 'S', 'TCG': 'S',
                  'TAT': 'I', 'TAC': 'M', 'TAA': 'I', 'TAG': 'I', 'TGT': 'T', 'TGC': 'T', 'TGA': 'U', 'TGG': 'T',
                  'CTT': 'E', 'CTC': 'E', 'CTA': 'D', 'CTG': 'D', 'CCT': 'G', 'CCC': 'G', 'CCA': 'G', 'CCG': 'G',
                  'CAT': 'V', 'CAC': 'V', 'CAA': 'V', 'CAG': 'V', 'CGT': 'A', 'CGC': 'A', 'CGA': 'A', 'CGG': 'A',
                  'ATT': '-', 'ATC': '-', 'ATA': 'Y', 'ATG': 'Y', 'ACT': '-', 'ACC': 'W', 'ACA': 'W', 'ACG': 'Y',
                  'AAT': 'L', 'AAC': 'L', 'AAA': 'F', 'AAG': 'F', 'AGT': 'S', 'AGC': 'S', 'AGA': 'S', 'AGG': 'S',
                  'GTT': 'Q', 'GTC': 'Q', 'GTA': 'H', 'GTG': 'H', 'GCT': 'R', 'GCC': 'R', 'GCA': 'R', 'GCG': 'R',
                  'GAT': 'L', 'GAC': 'L', 'GAA': 'L', 'GAG': 'L', 'GGT': 'P', 'GGC': 'P', 'GGA': 'P', 'GGG': 'P'}
    traducir = 0;

    with gzip.open(fasta, 'r') as f:
        for line in f:
            line=line.decode()
            if line[0] != '>':
                print (line[0:3:3])
                #traducir += line
            if traducir == 3:
                traducir = 0;
                print(traducir)

readFasta(sys.argv[1])