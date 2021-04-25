from math import sqrt


def num_key():
    print("Введите, пожалуйста, число ")
    num = int(input())
    print("Вы ввели число " + str(num))

def snt_in_mtr():
    print("Введите, пожалуйста, число сантиметров ")
    num = int(input())
    mtr = num // 100 # находим целую чатсь от деления на 100
    print("В " + str(num) + " сантиметрах(е) " + str(mtr) + " метр(ов)")

def fun_geron():
    print("Вам будет предложено ввести стороны треугольника")
    print("Введите a")
    a = int(input())
    print("Введите b")
    b = int(input())
    print("Введите c")
    c = int(input())
    p = (a + b + c) / 2 # находим полупериметр
    S = sqrt(p * (p - a) * (p - b) * (p - c)) # находим площадь
    print("Для треугольника со сторонами " + str(a) + " " + str(b) + " " + str(c) + " площадь равна " + str(S))

print("Задание 1")
num_key()

print("Задание 2")
snt_in_mtr()

print("Задание 3")
fun_geron()