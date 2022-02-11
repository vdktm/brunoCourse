filmTop = []

while True:
    addFilm = (input('Press name film: '))
    if addFilm == 'q':
        print('Your films added')
        print(filmTop)
        break
    filmTop.append(addFilm)



# num = []
#
# while True:
#     numIn = (input('Введите число: '))          #пользователь вводит число с клавиатуры
#     if numIn == 'q':
#         print('Сумма чисел равна:', sum(num))   #если ввели q тогда выводим сумму чисел в списке
#         break
#     num.append(int(numIn))