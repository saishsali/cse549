def find_occurences(text, ch):
    # Find all occurences of character ch in string text
    return [i for i, letter in enumerate(text) if letter == ch]

def last_to_first(transform, i):
    # Get position LastToFirst(i) in first column in the Burrows-Wheeler matrix for a given transform
    ch = transform[i]
    occurence = find_occurences(transform, ch).index(i)
    return sorted(transform).index(ch) + occurence

transform = raw_input()
i = int(raw_input())
print last_to_first(transform, i)

