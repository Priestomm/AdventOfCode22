import math

with open('./data/items', 'r') as items:
    compartments = items.readlines()

prior = 0


def priority(char):
    if ord(char) < 97:
        return ord(char) - 65 + 27

    return ord(char) - 96


for item in compartments:
    item = item.replace('\n', '')
    firstComp = item[slice(0, int(len(item) / 2))]
    secondComp = item[slice(int(len(item) / 2), len(item))]
    for ch in firstComp:
        if ch in secondComp:
            commonChar = ch
    prior += priority(commonChar)

elf = 0
groupsOfItems = list()

for i, item in enumerate(compartments):
    item = item.replace('\n', '')
    if i % 3 == 0:
        groupsOfItems.append(list())
    groupsOfItems[math.floor(i / 3)].append(item)

prior = 0

for group in groupsOfItems:
    firstRow = group[0]
    secondRow = group[1]
    thirdRow = group[2]

    for ch in firstRow:
        if ch in secondRow and ch in thirdRow:
            print(ch)
            prior += priority(ch)
            break
input(prior)
