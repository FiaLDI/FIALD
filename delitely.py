# Задаём функцию
def delet(x):
    # Создаём список с 1 и x
    lst = [1, x]
    # Добавление в список чисел в ранже от 2 до квадратного корня заданного числа
    for i in range(2, 1 + int(x ** 0.5)):
        if x % i == 0:
            lst.extend({x // i, i})
    return sorted(lst)


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print(delet(x))
print(delet(y))


#  Создаёт функцию которая из полученных списков создаёт множество и считает их пересечение
def obp(x, y):
    a = set(delet(x))
    b = set(delet(y))
    c = b.intersection(a)
    print(c)


print(obp(x, y))
