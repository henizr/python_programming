import pandas as pd

def readFile():
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)

def findData(data):
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if data in line:
                print(line)

def saveData(data):
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(data)

def changeData(data, modData):
    dataList =[]
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
            newList = line.strip()
            dataList.append(newList)

    for newLine in dataList:
        if data in newLine:
            index = dataList.index(newLine)
            dataList[index] = newLine.replace(data, modData)

    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in dataList:
            f.write(line + '\n')

def delData(data):
    dataList =[]
    with open('book.txt', 'r', encoding='utf-8') as f:
        for line in f:
            newList = line.strip()
            dataList.append(newList)

    for newLine in dataList:
        if data in newLine:
            index = dataList.index(newLine)
            del dataList[index]

    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in dataList:
            f.write(line + '\n')

def convertDataToCsv():
    df = pd.read_csv('book.txt')
    df.to_csv('book.csv', index=None)

while True:
    print("Телефонный справочник")
    print('1 - Прочитать данные')
    print('2 - Добавить и сохранить данные')
    print('3 - Найти данные')
    print("4 - Изменить данные")
    print("5 - Удалить данные")
    print("6 - Конвертировать данные в CSV")
    print("0 - Выйти")

    number = int(input('->'))
    
    if number == 0:
        break
    elif number == 1:
        readFile()
    elif number == 2:
        data = input('->')
        saveData(data + "\n")
    elif number == 3:
        data = input('->')
        findData(data)
    elif number == 4:
        data = input("Что изменить: ")
        modData = input("На что изменить: ")
        changeData(data, modData)
    elif number == 5:
        data = input("Что удалить: ")
        delData(data)
    elif number == 6:
        convertDataToCsv()

