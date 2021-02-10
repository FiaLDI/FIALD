sins = {"0": "0",
         "1/2":"pi/6",
         "sqrt(2)/2":"pi/4",
         "sqrt(3)/2":"pi/3",
         "1":"pi/2",
         "3pi/2": "-1"
         }
coss = {"1": "0",
            "sqrt(3)/2":"pi/6",
            "sqrt(2)/2":"pi/4",
            "1/2":"pi/3",
            "0":"pi/2",
            "-1":"pi",
            }
tgg = {"0": "0",
           "sqrt(3)/3":"pi/6",
           "1":"pi/4",
           "sqrt(3)":"pi/3",
           }
print("Решает уравнения вида cosx=b")
print("1 - sinx, 2 - cosx, 3 - tgx 0 - выход")


def uravnsin(b):
    sinx=b
    x = sins.get(sinx)
    print(x)

def uravncos(b):
    cosx=b
    x = coss.get(cosx)
    print(x)

def uravntg(b):
    tgx=b
    x = coss.get(tgx)
    print(x)

run=True
while run:
    try:
        operacia=int(input("Введите операцию: "))
        if operacia==1:
            b = input("Введите b: ")
            uravnsin(b)
        if operacia==2:
            r=input("Введите b: ")
            uravncos(r)
        if operacia==3:
            d=input("Введите b: ")
            uravntg(d)
        if operacia==0:
            run=False
    except:
        print("Ошибка.")






