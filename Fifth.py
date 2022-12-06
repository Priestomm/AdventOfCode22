import string

with open("./data/fifth", 'r') as data:
    raw = data.read()
    stacks = raw.split('\n\n')[0]
    moves = raw.split('\n\n')[1]

posToStack = [1, 5, 9, 13, 17, 21, 25, 29, 33]
containers = [list() for _ in range(10)]

for s in stacks.split('\n'):
    for i, ch in enumerate(s):
        if ch in string.ascii_uppercase:
            containers[posToStack.index(i)].append(ch)
for container in containers:
    container.reverse()

for move in moves.split('\n'):
    for letter in string.ascii_lowercase:
        move = move.replace(letter, '')
    move = move.split(' ')
    toMove = int(move[1])
    moveFrom = int(move[3]) - 1
    moveTo = int(move[5]) - 1
    crane = list()
    for _ in range(toMove):
        crane.append(containers[moveFrom].pop())
    crane.reverse()
    for el in crane:
        containers[moveTo].append(el)

print(containers)