from math import sqrt
sluchai={"1":"Линейные уравнения вида ax+b=0",
         "2":"Квадратные уравнения вида ax**2+bx+c= 0",
         "3":"Логарифмические уравнения решаемые по определению"}

def linaxb(a,b):
    x=-b/a
    print("Решение: ", x)

def kvadrat(a,b,c):
    D=b**2 - 4 * a * c
    print("Дискриминант:", D)
    x1=-b+sqrt(D)/2*a
    x2=-b-sqrt(D)/2*a
    print("Корень уравнения 1 -", x1)
    print("Корень уравнения 1 -", x2)

def logar(a, b):
    x=a**b
    if x>0 and a>1 and a != 1:
        print("Корень уравнения -", x)
    else:
        print("Нельзя")

znachenie=int(input("Введите операцию: "))
if znachenie==1:
    print(sluchai.get("1"))
    linaxb(a=int(input("Введите аргумент a: ")), b=int(input("Введите аргумент b: ")))
if znachenie==2:
    print(sluchai.get("2"))
    kvadrat(a=int(input("Введите аргумент a: ")), b=int(input("Введите аргумент b: ")), c=int(input("Введите аргумент c: ")))
if znachenie==3:
    print(sluchai.get("3"))
    logar(a=int(input("Введите аргумент a: ")), b=int(input("Введите аргумент b: ")))


