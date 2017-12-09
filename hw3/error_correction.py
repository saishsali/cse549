def complement(read):
    reverse_complement = ""
    for char in read:
        if char == 'A':
            reverse_complement += 'T'
        elif char == 'C':
            reverse_complement += 'G'
        elif char == 'G':
            reverse_complement += 'C'
        elif char == 'T':
            reverse_complement += 'A'
    return reverse_complement[::-1]

def hamming_distance(read1, read2):
    count = 0;
    for i in xrange(len(read1)):
        if read1[i] != read2[i]:
            count += 1
    return count

def error_correction(reads):
    correct_reads, incorrect_reads, corrections = [], [], []
    for read in reads:
        if reads.count(read) > 1:
            correct_reads.append(read)
        elif complement(read) in reads:
            correct_reads.append(read)
        else:
            incorrect_reads.append(read)

    for incorrect_read in incorrect_reads:
        for correct_read in correct_reads:
            if hamming_distance(incorrect_read, correct_read) == 1:
                corrections.append(incorrect_read + '->' + correct_read)
                break
            elif hamming_distance(incorrect_read, complement(correct_read)) == 1:
                corrections.append(incorrect_read + '->' + complement(correct_read))
                break

    return corrections


reads, i = [], 0

f = open('input.txt', 'r')
for line in f:
    if ">Rosalind_" in line:
        i = i + 1
    else:
        reads.append(line[:-1])
f.close()

corrections = error_correction(reads)
f = open('output.txt', 'w')
for correction in corrections:
    f.write("%s\n" % (correction))
f.close()
