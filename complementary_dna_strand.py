import dna_validation


def complementary(c):
    if c == 'A':
        return 'T'
    elif c == 'T':
        return 'A'
    elif c == 'C':
        return 'G'
    elif c == 'G':
        return 'C'


def complementary_dna(seq):
    comp_dna = ""
    if "Not found valid DNA sequence" in dna_validation.validate_dna(seq):
        return "Not found complementary DNA strand"
    else:
        for i in range(0, len(seq), 1):
            comp_dna += complementary(seq[i])
        return "Complementary DNA strand: "+str(comp_dna)


if __name__ == '__main__':
    # reading DNA seq from Fasta file and validating it
    file_dna = open("data/dna_sequence_valid.fa", 'r', 1)
    seqDNA = ""
    file_dna.readline()  # skip the first line (desc in Fasta files)
    for line in file_dna:
        seqDNA += line
    seqDNA = seqDNA.replace('\n', '')
    file_dna.close()
    print(dna_validation.validate_dna(seqDNA))
    print(complementary_dna(seqDNA))
