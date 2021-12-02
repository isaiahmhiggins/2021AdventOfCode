file = open('Real.txt')
content = file.readlines()
answer = 0
win = []
for i in range(0, len(content) - 2):
    win += [int(content[i]) + int(content[i+1]) + int(content[i+2])]
for i in range(1, len(win)):
    prev = win[i -1]
    current = win[i]
    compare = int(current) - int(prev)
    if(compare > 0):
        answer += 1

    
print(answer)