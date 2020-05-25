adenine = 'A'
thymine = 'T'
guanine = 'G'
cytosine = 'C'
uracil = 'U'

start = "ATG"
end1 = "TAA"
end2 = "TAG"
end3 = "TGA"


def validate_dna(seq):
    check_dna = True
    for i in range(1, len(seq), 1):
        if not ((seq[i] == adenine) or (seq[i] == thymine) or (seq[i] == guanine) or (seq[i] == cytosine)):
            check_dna = False

    s = 0  # start
    e = 0  # end

    found_start = False
    found_end = False

    if check_dna:
        for i in range(0, len(seq) - 2, 3):
            if not found_start:
                if seq[i:i + 3] == start:
                    found_start = True
                    s = i
            if found_start:
                if seq[i:i + 3] == end1 or seq[i:i + 3] == end2 or seq[i:i + 3] == end3:
                    found_end = True
                    e = i

    if found_start and found_end:
        seq = seq[s:e + 3]
        return "Valid DNA sequence: "+str(seq)
    else:
        return "Not found valid DNA sequence"


if __name__ == '__main__':
    # reading DNA seq from Fasta file and validating it
    file_dna = open("data/dna_sequence_valid.fa", 'r', 1)
    seqDNA = ""
    file_dna.readline()  # skip the first line (desc in Fasta files)
    for line in file_dna:
        seqDNA += line
    seqDNA = seqDNA.replace('\n', '')
    file_dna.close()
    print(validate_dna(seqDNA))
