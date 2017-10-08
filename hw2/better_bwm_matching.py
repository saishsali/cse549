def count_symbol(symbol, i, last_column):
    # Returns the number of occurrences of symbol in the first i positions of last_column
    return last_column[:i].count(symbol)

def bwm_matching(first_occurence, last_column, pattern):
    # Count the total number of matches of Pattern in Text
    top = 0
    bottom = len(last_column) - 1

    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in last_column[top:bottom + 1]:
                top = first_occurence[symbol] + count_symbol(symbol, top, last_column)
                bottom = first_occurence[symbol] + count_symbol(symbol, bottom + 1, last_column) - 1
            else:
                return 0
        else:
            return bottom - top + 1

def get_first_occurence(last_column):
    # First occurence is the first position of symbol in first_column
    first_column = ''.join(sorted(last_column))
    unique_symbols = ''.join(set(first_column))
    first_occurence = {}
    for c in unique_symbols:
        first_occurence[c] = first_column.find(c)
    return first_occurence

def get_num_substrings(last_column, patterns):
    # Get a list of total number substring matches for all patterns
    first_occurence = get_first_occurence(last_column)
    num_substring = []
    for pattern in patterns:
        num_substring.append(bwm_matching(first_occurence, last_column, pattern))
    return " ".join(str(s) for s in num_substring)

f = open('input.txt', 'r')
last_column = f.readline()[:-1]
patterns = f.readline()[:-1].split()
f.close()

f = open('output.txt', 'w')
f.write(get_num_substrings(last_column, patterns))
f.close()
