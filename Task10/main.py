n = int(input('n->'))
result = 0

for i in range(n):
    m = int(input(f'm{i}->'))
    if m == 0:
        result += 1

print(result)