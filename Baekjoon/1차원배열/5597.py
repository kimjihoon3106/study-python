values = []
non_values = []

for i in range(28):
    num = int(input())
    values.append(num)

for i in range(1, 31):
    if i not in values:
        non_values.append(i)

non_values.sort()

print(non_values[0])
print(non_values[1])