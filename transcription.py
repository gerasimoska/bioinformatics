# Transcription is the first step in gene expression.
# It involves copying a gene's DNA sequence to make an RNA molecule.

from Bio import SeqIO


def read_fasta(path):
    seq = ""
    for record in SeqIO.parse(path, "fasta"):
        seq = record.seq.upper()
    return seq


adenine = 'A'
thymine = 'T'
guanine = 'G'
cytosine = 'C'
start = "ATG"
end1 = "TAA"
end2 = "TAG"
end3 = "TGA"


def complementary(c):
    if c == 'A':
        return 'U'
    elif c == 'T':
        return 'A'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'


def transcription(dna):
    rna = ""
    for i in range(0, len(dna)):
        rna += complementary(dna[i])
    return rna


if __name__ == '__main__':
    seq_dna = read_fasta("data/sequence1.fasta")
    print("DNA sequence:")
    print(seq_dna)
    print("Complementary RNA sequence:")
    print(transcription(seq_dna))
