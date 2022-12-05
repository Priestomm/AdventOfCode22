with open("./data/fourth", 'r') as data:
    pairs = data.readlines()

totOL = 0
partOL = 0
for line in pairs:
    firstElf = line.split(',')[0]
    secondElf = line.split(',')[1]
    firstSec = list(i for i in range(int(firstElf.split('-')[0]), int(firstElf.split('-')[1]) + 1))
    secondSec = list(i for i in range(int(secondElf.split('-')[0]), int(secondElf.split('-')[1]) + 1))
    if (min(firstSec) <= min(secondSec) and max(firstSec) >= max(secondSec)) or (min(secondSec) <= min(firstSec) and max(secondSec) >= max(firstSec)):
        totOL += 1
    if any(a in set(secondSec) for a in firstSec):
        partOL += 1

input(totOL)
input(partOL)