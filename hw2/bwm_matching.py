def find_occurences(text, ch):
    # Find all occurences of character ch in string text
    return [i for i, letter in enumerate(text) if letter == ch]

def last_to_first(transform, i):
    # Get position LastToFirst(i) in first column in the Burrows-Wheeler matrix for a given transform
    ch = transform[i]
    occurence = find_occurences(transform, ch).index(i)
    return sorted(transform).index(ch) + occurence

def bwm_matching(transform, pattern, l2f):
    # Count the total number of matches of Pattern in Text
    top = 0
    bottom = len(transform) - 1

    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in transform[top:bottom + 1]:
                top_index = transform[top:bottom + 1].find(symbol) + top
                bottom_index = transform[top:bottom + 1].rfind(symbol) + top
                top = l2f[top_index]
                bottom = l2f[bottom_index]
            else:
                return 0
        else:
            return bottom - top + 1

def num_substring(transform, patterns):
    # Get a list of total number substring matches for all patterns
    l2f = []
    for i in xrange(0, len(transform)):
        l2f.append(last_to_first(transform, i))

    num_substring = []
    for pattern in patterns:
        num_substring.append(bwm_matching(transform, pattern, l2f))

    return num_substring

f = open('input.txt', 'r')
transform = f.readline()[:-1]
patterns = f.readline()[:-1].split()
f.close()

f = open('output.txt', 'w')
f.write(" ".join(str(s) for s in num_substring(transform, patterns)))
f.close()
