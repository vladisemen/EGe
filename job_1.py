def summ():
    sum = 0 #сумма всех элементов
    x = 2   #счетчик цикла
    while(x<=149):
        sum = sum + (1 / x)
        x = x + 3
    return sum

def ameba(num):
    i = 0
    ameb = 1 #сумма всех амеб
    while i < num:
        ameb = ameb * 2 #умножаем амебу на 2
        i = i + 3
    return ameb

def sport():
    s = 10 #расстояне в конкретный день
    sum = 10 #расстояне всего
    i = 1
    while i < 7:
        s = s + s / 10
        sum = sum + s
        i = i + 1
    return sum

print("Задание 1: Сумма ряда = " + str(summ()))
print("Задание 2:")
x = 3
while x<=24:
    print("Через " + str(x) + " час(ов, са) будет " + str(ameba(x)) + " клеток" )
    x = x + 3
print("Задание 3: Спортсмен пробежал = " + str(sport()))