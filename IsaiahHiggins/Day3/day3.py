import sys
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com

content = com.readAndCleanLine('Real.txt')
#content = com.readAndCleanLine('sample.txt')

def filterResults(pos, list, filter):
    result = []
    for line in list:
        if line[pos] == filter:
            result += [line]
    return result

def findLevel(data, control):
    columns = com.getCol(data)
    for row in range(0, len(columns)):
        if len(data) > 1:
            if control == 'oxygen':
                if(columns[row].count('1') >= columns[row].count('0')):
                    data = filterResults(row, data, '1')
                else:
                    data = filterResults(row, data, '0')
            elif control == 'co2':
                if(columns[row].count('1') < columns[row].count('0')):
                    data = filterResults(row, data, '1')
                else:
                    data = filterResults(row, data, '0')
            columns = com.getCol(data)
        else:
            break        
    return int(data[0], 2)


oxygen = findLevel(content, 'oxygen')
co2 = findLevel(content, 'co2')
print(oxygen)
print(co2)
print(co2*oxygen)
