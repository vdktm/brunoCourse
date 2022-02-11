
userDict = {}
name = ''
newDict = {}

print("Для выхода из программы, введите 'q' два раза")

while not name == 'q':
    name = input('Введите имя: ')
    tele = input('Введите номер телефона: ')
    userDict[name] = tele

for name in userDict.keys():
    if name[0] == 'А':
        newDict[name] = userDict[name]
print(newDict)