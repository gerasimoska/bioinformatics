adenine = 'A'
thymine = 'T'
guanine = 'G'
cytosine = 'C'
uracil = 'U'

start = "AUG"
end1 = "UAA"
end2 = "UAG"
end3 = "UGA"


def validate_rna(seq):
    check_rna = True
    for i in range(1, len(seq), 1):
        if not seq[i] == adenine or seq[i] == uracil or seq[i] == guanine or seq[i] == cytosine:
            check_rna = False

    s = 0  # start
    e = 0  # end

    found_start = False
    found_end = False

    if check_rna:
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
        return "Valid rna sequence: "+str(seq)
    else:
        return "Not found valid rna sequence"


if __name__ == '__main__':
    # reading rna seq from Fasta file and validating it
    file_rna = open("data/rna_sequence_valid.ma", 'r', 1)
    seq_rna = ""
    file_rna.readline()  # skip the first line (desc in Fasta files)
    for line in file_rna:
        seq_rna += line
    seq_rna = seq_rna.replace('\n', '')
    file_rna.close()
    print(validate_rna(seq_rna))
