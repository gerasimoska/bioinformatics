import random
from transcription import read_fasta
from translation import protein_sequence

adenine = "A"
thymine = "T"
guanine = "G"
cytosine = "C"
start = "ATG"
end1 = "TAA"
end2 = "TAG"
end3 = "TGA"


def random_mutation(seq):
    seq = list(seq)
    nucleotides = ["A", "T", "C", "G"]
    pos = random.randint(0, len(seq))
    char = nucleotides[random.randint(0, 3)]
    if seq[pos] != char:
        seq[pos] = char
    else:
        char = nucleotides[random.randint(0, 3)]
        seq[pos] = char
    res = ""
    for i in range(0, len(seq)):
        res += seq[i]
    return res


if __name__ == "__main__":
    seq_dna = read_fasta("data/brca1.fasta")
    mutation = random_mutation(seq_dna)
    print(protein_sequence(mutation))
