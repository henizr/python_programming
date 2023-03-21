n = int(input("введите количество элементов->"))
array = []
counter = 0

for i in range(n):
    num = int(input(f"число {i}->"))
    array.append(num)

x = int(input("x->"))

for i in array:
    if x == i:
        counter += 1

print(f"-> {counter}")