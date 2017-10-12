diagonal, top, left = 1, 2, 3
score_match = 10
score_mismatch = -5
score_gap = -7

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
        return score_match
    else:
        return score_mismatch

def path_taken(choice):
    # Optimal path taken can be diagonal, top or left
    if choice == 2:   # Diagonal
        return diagonal
    elif choice == 0: # Top
        return top
    elif choice == 1: # Left
        return left

def compute_opt(mat, max_gap, s, t):
    max1, max2, max3 = 0, 0, 0
    # Compute edit distance matrix and alignment path matrix
    for i in xrange(1, len(s) + 1):
        for j in xrange(1, len(t) + 1):
            choices = [
                score_gap + mat[i - 1][j],
                score_gap + mat[i][j - 1],
                match_cost(s[i - 1], t[j - 1]) + mat[i - 1][j - 1]
            ]
            mat[i][j] = max(choices)
            print s[i - 1], t[j - 1]
            print mat
            if mat[i][j] == choices[0]:
                print "Top"
                max1 = max_gap[i - 1][j]
            if mat[i][j] == choices[1]:
                print "Left"
                max2 = max_gap[i][j - 1]
            if mat[i][j] == choices[2]:
                print "Diagonal"
                max3 = max_gap[i - 1][j - 1]
            max_gap[i][j] = max(max1, max2, max3)
    # print mat

def edit_distance_alignment(s, t):
    # Compute edit distance alignment
    mat = []
    initialize_matrix(mat, s, t)
    base_case(mat, s, t)

    max_gap = []
    initialize_matrix(max_gap, s, t)
    base_case(max_gap, s, t)

    compute_opt(mat, max_gap, s, t)

    return max_gap[len(s)][len(t)]


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
# edit_distance, aligned_s, aligned_t = edit_distance_alignment(s, t)
print edit_distance_alignment(s, t)
# f.write("%d\n%s\n%s" % (edit_distance, aligned_s, aligned_t))
f.close()
