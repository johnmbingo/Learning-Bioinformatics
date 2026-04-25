Nucleotides = ["A", "C", "G", "T"]
#Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

#to count nucleotide frequency
def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

#Personal attempt to define a function to transcribe DNA to RNA. I know there is a built in function for this but I wanted to try it myself.
def transcribeDNAtoRNA(seq):
    for nuc in seq:
        seq = seq.replace("T","U")
    return seq
