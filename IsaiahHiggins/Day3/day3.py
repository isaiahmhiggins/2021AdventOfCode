import sys
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com

#content = com.readAndCleanLine('Real.txt')
content = com.readAndCleanLine('sample.txt')

def filterResults(pos, list, filter):
    result = []
    for line in list:
        if line[pos] == filter:
            result += [line]
    return result

def findLevel(data, control = None):
    for row in range(0, len(data[1])):
        col = []
        if len(data) > 1:
            for line in data:
                col += line[row]
            if len(data) > 1:
                if control == 'oxygen':
                    if(col.count('1') >= col.count('0')):
                        data = filterResults(row, data, '1')
                    else:
                        data = filterResults(row, data, '0')
                elif control == 'co2':
                    if(col.count('1') < col.count('0')):
                        data = filterResults(row, data, '1')
        else:
            break        
    return int(data[0], 2)


oxygen = findLevel(content, 'oxygen')
co2 = findLevel(content, 'co2')
print(oxygen)
print(co2)
print(co2*oxygen)

