firstCol = ['A', 'B', 'C']
secondCol = ['X', 'Y', 'Z']
letToSign = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}


def whoWin(opp, me):
    retPoints = secondCol.index(me) + 1
    print(letToSign.get(opp), "vs", letToSign.get(me))
    print("Point for sign -> +", retPoints)
    if secondCol.index(me) == firstCol.index(opp):
        retPoints += 3
        print("Draw -> + 3")
    elif (firstCol.index(opp) + 1) % 3 == secondCol.index(me):
        retPoints += 6
        print("Win -> + 6")

    return retPoints


def whoWin2(opp, res):
    retPoints = 0
    if res == 'X':
        print("You must lose")
        retPoints += ((firstCol.index(opp) + 2) % 3) + 1

    elif res == 'Y':
        print("You must draw")
        retPoints += 3
        retPoints += firstCol.index(opp) + 1
    else:
        print("You must win")
        retPoints += 6
        retPoints += ((firstCol.index(opp) + 1) % 3) + 1

    return retPoints


points = 0

for i, line in enumerate(open('./data/rps', 'r').readlines()):
    print("Round ", i)
    points += whoWin(line[0], line[2])
    print("Total points", points)
    print("------------------------------------")

points = 0

for i, line in enumerate(open('./data/rps', 'r').readlines()):
    print("Round ", i)
    points += whoWin2(line[0], line[2])
    print("Total points", points)
    print("------------------------------------")

input()
