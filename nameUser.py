
userDict = {}
name = ''
newDict = {}

print("Для выхода из программы, введите 'q' два раза")

while True:
    name = input('Введите имя: ')
    if name == 'q':
        break
    tele = input('Введите номер телефона: ')
    userDict[name] = tele

for name in userDict.keys():
    if name[0] == 'A':
        newDict[name] = userDict[name]

print(newDict)

