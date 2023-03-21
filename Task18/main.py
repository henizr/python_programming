n = int(input("введите количество элементов->"))
array = []
result = 0

for i in range(n):
    num = int(input(f"число {i}->"))
    array.append(num)

x = int(input("x->"))

if x in array:
    print(f"->{x}")
else:
    for i in range(len(array)-1):
        minVal = i
        for j in range(i+1, len(array)):
            if array[j] < array[minVal]:
                minVal = j
        temp = array[i]
        array[i] = array[minVal]
        array[minVal] = temp
    for i in range(len(array)):
        if array[i] > x:
            result = array[i-1]
                           
    print(f"->{result}")