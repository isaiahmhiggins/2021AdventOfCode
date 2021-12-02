import networkx as nx

def readAndCleanLine(file):
    result = []
    f = open(file)
    content = f.readlines()
    for i in range(0, len(content)):
        result += content[i].replace('\n', '')
    return result
