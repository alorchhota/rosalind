import sys
import collections

def countNucleotides(dna):
    """ count neuclides in a dna string"""
    counter = collections.Counter(dna)
    return {c:counter[c] for c in 'ACGT'}

# formated I/O
if __name__ == "__main__":
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
        dna = lines[0]
        freq = countNucleotides(dna)

        with open(sys.argv[2], 'w') as outFile:
            outStr = ' '.join([str(freq[c]) for c in 'ACGT'])
            outFile.write(outStr)
        

