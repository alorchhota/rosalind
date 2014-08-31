import sys
from Dna import *

# format I/O
if __name__ == '__main__':
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
        dna = Dna(lines[0].strip())
        rc = dna.revc()

    with open(sys.argv[2], 'w') as outFile:
        outFile.write(rc)




