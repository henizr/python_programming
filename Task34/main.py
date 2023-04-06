input_text = "пара-ра-рам рам-пам-папам па-ра-па-да"

def find(text):
    words = text.split()
    new_list = []
    counter = 0
    letters = "ауеёыоэяию"
    for word in words:
        for letter in word:
            if letter in letters:
                counter += 1
        new_list.append(counter)
        counter = 0
    result = new_list[0]
    for i in range(1, len(new_list)):
        if result != new_list[i]:
            return False
    return True

if  find(input_text):
    print("Парам пам-пам")
else:
    print("Пам парам")