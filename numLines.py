def numLines(num_lines, fname):
    with open(fname, ) as f:
        for line in f:
            words = line.split()

            num_lines += line.count(".")
    return num_lines
