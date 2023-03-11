number = int(input("Введите число: "))  

half_1 = 0
half_2 = 0

for i in range(3):
    half_1 += number % 10
    number = number // 10

for i in range(3):
    half_2 += number % 10
    number = number // 10

if (half_1 == half_2):
    print("Yes")
else:
    print("No")