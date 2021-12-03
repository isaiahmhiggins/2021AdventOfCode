import networkx as nx

def readAndCleanLine(file):
    result = []
    f = open(file)
    content = f.readlines()
    for i in range(0, len(content)):
        result += [content[i].replace('\n', '')]
    return result

def strToInt(array):
    return [int(x) for x in array]

def eachWord(file, splitChar):
    word = []
    f = open(file)
    content = f.readlines()
    for line in content:
        line = line.strip()
        word += line.split(splitChar)

    return word

def getCol(data):
    result = []
    for row in range(0, len(data[0])):
        col = []
        for line in data:
            col += line[row]
        result.append(col)
    return result

