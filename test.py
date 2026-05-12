def parse(inputstring):
    tempstringdict = {}

    #Need to split input string
    #Need to ID every key in the string
    #Associate or zip every value associated to the key
    #Need to count every occurance of the value

    
    for k in inputstring:
        tempstringdict[k] += 1
    return tempstringdict
    