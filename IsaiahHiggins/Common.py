def readAndClean(file):
    result = []
    f = open(file)
    content = file.readlines()
    for i in range(0, len(content)):
        result += content[i].replace('\n', '')
    return result
