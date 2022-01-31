num = []

while True:
    numIn = (input('Введите число: '))
    if numIn == 'q':
        print('Сумма чисел равна:', sum(num))
        break
    num.append(int(numIn))