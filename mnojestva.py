from typing import List, Any


def setlist(a):
    '''Вводит числа в список,
для того чтобы закончить
ввод - напишите любой символ отличный от цифры'''
    try:
        print("Введите числа списка")
        while True:
            x = int(input("Ввод: "))
            a.append(x)
    except:
        print("Список создан:", a)


def intersept(a, b):
    d = set(a)
    c = set(b)
    ar = d.intersection(c)
    print(ar)


def unio(a, b):
    d = set(a)
    c = set(b)
    ar = d.union(c)
    print(ar)


def diiffer(a, b):
    d = set(a)
    c = set(b)
    ar = d.difference(c)
    print(ar)


b = []
c = []
run = False

start = str(input("Запусите программу командой старт - "))
if start == "старт" or start == "start":
    run = True
    print("Запускается.")
    print(setlist.__doc__)
while run:
    setlist(b)
    setlist(c)
    usl = input("Введите операцию - [& , |, -] - ")
    if usl == "&":
        intersept(b, c)
        run = False
    elif usl == "|":
        unio(b, c)
        run = False
    elif usl == "-":
        diiffer(b, c)
        run = False
    else:
        run = False
