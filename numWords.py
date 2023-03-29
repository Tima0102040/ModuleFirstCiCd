def numWords(num_words, fname):
    with open(fname, ) as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    return num_words