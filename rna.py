import sys
import re

def transcribe(dna):
    """ transcription from dna to rna """
    return re.sub('T', 'U', dna)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as inFile:
        lines = inFile.readlines()
        dna = lines[0]
        rna = transcribe(dna)

        with open(sys.argv[2], 'w') as outFile:
            outFile.write(rna)
