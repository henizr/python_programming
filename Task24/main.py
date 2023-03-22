kusti = 4
yagodi = [1,2,3,4]
obj = {}

for i in range(len(yagodi)):
    if i == 0:
        newYagodi = yagodi[:]
        newYagodi.insert(0, newYagodi.pop())
        obj[f"{i}"] = newYagodi[i] + newYagodi[i+1] + newYagodi[i+2]
    elif i == len(yagodi) - 1:
         newYagodi = yagodi[:]
         newYagodi.insert(len(yagodi) - 1, newYagodi.pop(0))
         obj[f"{i}"] = newYagodi[i] + newYagodi[i-1] + newYagodi[i-2]
    else:
         newYagodi = yagodi[:]
         obj[f"{i}"] = newYagodi[i-1] + newYagodi[i] + newYagodi[i+1]

print(max(list(obj.values())))
