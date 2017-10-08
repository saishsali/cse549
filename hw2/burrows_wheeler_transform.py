def rotate(text):
    # Return a list of rotations for string text
    double_text = 2 * text
    return [ double_text[i:i + len(text)] for i in xrange(0, len(text))]

def burrows_wheeler_matrix(text):
    # Return a lexicographically sorted list of rotations for string text
    return sorted(rotate(text))

def burrows_wheeler_transform(text):
    # Return BWT by joining last column of BWM
    return ''.join(t[-1] for t in burrows_wheeler_matrix(text))

text = raw_input()
print(burrows_wheeler_transform(text))
