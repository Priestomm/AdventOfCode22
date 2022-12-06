with open("./data/sixth", 'r') as data:
    signal = data.read()

# Part 1
for offset, ch in enumerate(signal):
    setSig = set(signal[offset + i] for i in range(4))
    if len(setSig) == 4:
        res = 4 + offset
        break

input(res)

# Part 2
for offset, ch in enumerate(signal):
    setSig = set(signal[offset + i] for i in range(14))
    if len(setSig) == 14:
        res = 14 + offset
        break

input(res)