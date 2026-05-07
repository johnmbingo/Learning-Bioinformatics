import random
from DNAToolkit import *

nucleotides = ['A','T','G','C']
nuccompliments = {'A':'T','T':'A','G':'C','C':'G'}

#random DNA strings for testing

randomDNAstring = ''.join([random.choice(nucleotides)
                          for nuc in range(0,50)])

randomDNAstring2 = ""

for num in range (0,50):
    randomDNAstring2 += random.choice(nucleotides)

randomDNAstring3 = "".join(random.choice(nucleotides) for num in range(0,50))

#________________________________________________________ TOOLKIT ________________________________________________________________________________________________

#Used to validate if a sequence of letters are part of the nucleotides mentioned above

def validatesequence(inputDNAseq):
    for nuc in inputDNAseq:
        if nuc not in nucleotides:
            return False
    return inputDNAseq

#Testing = works
#A hint: create an temporary dictionary with 0 associated with the nucleotides

def countnucleotidesequence(inputDNAseq):
    tmpsequence = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for k in inputDNAseq:
        tmpsequence[k] += 1
    return tmpsequence

#Sticking point 1: when adding a for loop, simply name the dictionary and add the key within [], += will add whatever integer comes after it for the values
#Sticking point 2: The for loop applies to the inputDNAseq, make sure the for loop applies to the right thing
#Testing = works

#Transcribing DNA into RNA

#def transcribingDNAtoRNA(inputDNAseq):
    for nuc in inputDNAseq:
        inputDNAseq = inputDNAseq.replace('A','U')
    return(inputDNAseq)

def transcribingDNAtoRNA2(inputDNAseq):
    return inputDNAseq.replace('A', 'U')

#Simplify, this does not need a for loop
#Sticking point, in for loops when replacing individual items in strings, make sure to apply this syntax: oldstring = oldstring.replace('item being replaced','item that is replacing')

#Reverse compliment

def reversecompliment(inputDNAseq):
    return ''.join([nuccompliments[nuc] for nuc in inputDNAseq])[::-1]

#How do I tranlate this into a for loop that makes sense to me, create another iteration of the code

#def reversecompliment2(inputDNAseq):
    for nuc, com in nuccompliments:
        outputDNAseq = inputDNAseq.replace(nuc, com)
    return outputDNAseq

#____________________________________TESTING GROUNDS______________________________________












    