import sys



# format I/O
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
        rna = lines[0].strip()
        d = hamm(dna1, dna2)

    with open(sys.argv[2], 'w') as outFile:
        outFile.write(str(d))




