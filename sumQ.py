# Задача 1. Напишите программу, которая использует цикл,
# чтобы предложить пользователю ввести 5 чисел.
# Сложите их и выведите результат на экран.

#Задача 2. Дополните программу так,
#чтобы пользователь мог вводить произвольное количество чисел,
#а завершал их ввод символом 'q'.


num = []

while True:
    numIn = (input('Введите число: '))          #пользователь вводит число с клавиатуры
    if numIn == 'q':
        print('Сумма чисел равна:', sum(num))   #если ввели q тогда выводим сумму чисел в списке
        break
    num.append(int(numIn))                      #добавляем числа в список




