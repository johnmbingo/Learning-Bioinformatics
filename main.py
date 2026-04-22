from DNAToolkit import *
import random 

# Creating a random DNA seqence for testing
rndDNAstry = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

print(validateSeq(rndDNAstry))
print(countNucFrequency(rndDNAstry))
