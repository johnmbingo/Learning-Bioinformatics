outputFile = []

with open('UTube Informatics Tutorial/input.txt', 'r') as inputFile:
    outputFile = [line for pos, line in enumerate(inputFile) if pos % 2 != 0]

