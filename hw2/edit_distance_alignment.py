diagonal, top, left = 1, 2, 3

def initialize_matrix(mat, s, t):
    # Initialize m * n matrix with 0 (m = length of s + 1, n = length of t + 1)
    for i in xrange(len(s) + 1):
        row = []
        for j in xrange(len(t) + 1):
            row.append(0)
        mat.append(row)

def base_case(mat, s, t):
    # Aligning i characters to 0 characters must use i gaps
    for i in xrange(len(s) + 1):
        mat[i][0] = i

    for i in xrange(len(t) + 1):
        mat[0][i] = i

def match_cost(a, b):
    # Cost of match = 0, Cost of mismatch = 1
    if a == b:
        return 0
    else:
        return 1

def path_taken(choice):
    # Optimal path taken can be diagonal, top or left
    if choice == 2:   # Diagonal
        return diagonal
    elif choice == 0: # Top
        return top
    elif choice == 1: # Left
        return left

def compute_opt(mat, alignment_path, s, t):
    # Compute edit distance matrix and alignment path matrix
    for i in xrange(1, len(s) + 1):
        for j in xrange(1, len(t) + 1):
            choices = [
                1 + mat[i - 1][j],
                1 + mat[i][j - 1],
                match_cost(s[i - 1], t[j - 1]) + mat[i - 1][j - 1]
            ]
            mat[i][j] = min(choices)
            opt_choice = choices.index(mat[i][j])
            alignment_path[i][j] = path_taken(opt_choice)

    print mat
    print alignment_path

def get_alignment(alignment_path, s, t):
    # Compute the actual alignment of s and t
    i, j = len(s), len(t)
    aligned_s, aligned_t = [], []
    while True:
        if alignment_path[i][j] == diagonal:
            aligned_s.append(s[i - 1])
            aligned_t.append(t[j - 1])
            i = i - 1
            j = j - 1
        elif alignment_path[i][j] == top:
            aligned_s.append(s[i - 1])
            aligned_t.append('-')
            i = i - 1
        elif alignment_path[i][j] == left:

            aligned_s.append('-')
            aligned_t.append(t[j - 1])
            j = j - 1
        elif i == 0 and j == 0:
            break

    return ''.join(aligned_s[::-1]), ''.join(aligned_t[::-1])


def edit_distance_alignment(s, t):
    # Compute edit distance alignment
    mat = []
    initialize_matrix(mat, s, t)
    base_case(mat, s, t)

    alignment_path = []
    initialize_matrix(alignment_path, s, t)

    compute_opt(mat, alignment_path, s, t)
    aligned_s, aligned_t = get_alignment(alignment_path, s, t)

    return mat[len(s)][len(t)], aligned_s, aligned_t


proteins, i = ['', ''], -1

f = open('input.txt', 'r')
for line in f:
    if ">Rosalind_" in line:
        i = i + 1
    else:
        proteins[i] += line[:-1]
f.close()

s, t = proteins[0], proteins[1]

f = open('output.txt', 'w')
edit_distance, aligned_s, aligned_t = edit_distance_alignment(s, t)
f.write("%d\n%s\n%s" % (edit_distance, aligned_s, aligned_t))
f.close()
