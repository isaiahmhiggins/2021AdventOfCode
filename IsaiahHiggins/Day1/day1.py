file = open('Real.txt')
content = file.readlines()
answer = 0
win = []
for i in range(0, len(content) - 2):
    content = [int(x) for x in content]
    win += [sum(content[i:i+2])]
for i in range(1, len(win)):
    prev = win[i -1]
    current = win[i]
    if(current > prev):
        answer += 1

    
print(answer)