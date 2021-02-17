# Sinus Dictionary
sins = {"0": "0",
        "1/2": "pi/6",
        "sqrt(2)/2": "pi/4",
        "sqrt(3)/2": "pi/3",
        "1": "pi/2",
        "3pi/2": "-1"
        }


# Cossinus Dictionary
coss = {"1": "0",
        "sqrt(3)/2": "pi/6",
        "sqrt(2)/2": "pi/4",
        "1/2": "pi/3",
        "0": "pi/2",
        "-1": "pi",
        }


# tangens Dictionary
tgg = {"0": "0",
       "sqrt(3)/3": "pi/6",
       "1": "pi/4",
       "sqrt(3)": "pi/3",
       }


print("Solves equations of the form  cosx=b")
print("1 - sinx, 2 - cosx, 3 - tgx 0 - exit")


# The function that solves the equation (1)
def uravnsin(b):
    sinx = b
    x = sins.get(sinx)
    print(x)


# The function that solves the equation (2)
def uravncos(b):
    cosx = b
    x = coss.get(cosx)
    print(x)


# The function that solves the equation (3)
def uravntg(b):
    tgx = b
    x = coss.get(tgx)
    print(x)



# Loop Solving Equation
runing = True
while runing:
    try:
        operation = int(input("Enter operation: "))
        if operation == 1:
            b = input("Enter b: ")
            uravnsin(b)
        if operation == 2:
            r = input("Enter b: ")
            uravncos(r)
        if operation == 3:
            d = input("Enter b: ")
            uravntg(d)
        if operation == 0:
            runing = False
    except:
        print("Error.")
