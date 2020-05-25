from Bio import SeqIO
from transcription import read_fasta


adenine = 'A'
thymine = 'T'
guanine = 'G'
cytosine = 'C'
start = "ATG"
end1 = "TAA"
end2 = "TAG"
end3 = "TGA"

acids = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "", "TAG": "",
    "TGC": "C", "TGT": "C", "TGA": "*", "TGG": "W",
}


def amino_acids(seq):
    for key in acids.keys():
        if seq == key:
            return acids[key]


def protein_sequence(seq):
    protein = ""
    for i in range(0, len(seq) - 3, 3):
        if amino_acids(seq[i:i + 3]) is not None:
            protein += amino_acids(seq[i:i + 3])
    return protein


if __name__ == '__main__':
    dna_seq = read_fasta("data/brca1.fasta")
    print("Length of BRCA1 sequence:" + str(len(dna_seq)))
    print("First 90 nucleotides: " + dna_seq[0:90])
    print("Protein sequence: " + protein_sequence(dna_seq))
    print("First 30 amino acids: " + protein_sequence(dna_seq)[0:30])
