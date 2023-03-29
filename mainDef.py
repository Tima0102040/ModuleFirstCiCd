def numLinesAndWords(num_lines, num_words, fname):
    with open(fname, ) as f:
        for line in f:
            words = line.split()

            num_lines += line.count(".")
            num_words += len(words)
    print('Кількість слів у файлі: ', num_words)
    print('Кількість речень у файлі: ', num_lines)
