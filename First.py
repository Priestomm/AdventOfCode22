
lines = open('./data/calories', 'r').readlines()
calories = [0]
elf = 0

for line in lines:
    if line.strip():
        calories.insert(elf, calories.pop(elf) + int(line))
    else:
        elf += 1
        calories.insert(elf, 0)

print(calories)
print(f"The elf number {calories.index(max(calories))} brings {max(calories)} calories")
