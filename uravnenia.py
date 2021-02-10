from math import sqrt


#Function dictionary
sluchai = {"1": "Linear equations of the form  ax+b=0",
           "2": "Quadratic equations of the form  ax**2+bx+c= 0",
           "3": "Logarithmic equations solved by definition "}


#Solving Equations (1)
def linaxb(a, b):
    x = -b / a
    print("Resolve: ", x)


#Solving Equations (2)
def kvadrat(a, b, c):
    D = b ** 2 - 4 * a * c
    print("Discriminant :", D)
    x1 = -b + sqrt(D) / 2 * a
    x2 = -b - sqrt(D) / 2 * a
    print("Root of the equation 1 -", x1)
    print("Root of the equation 2 -", x2)


#Solving Equations (3)
def logar(a, b):
    x = a ** b
    if x > 0 and a > 1 and a != 1:
        print("Root of the equation -", x)
    else:
        print("It is impossible ")

#Loop Solving Equation
run=True
while run:
    znachenie = int(input("Enter operation: "))
    if znachenie == 1:
        print(sluchai.get("1"))
        linaxb(a=int(input("Enter the argument a: ")), b=int(input("Enter the argument b: ")))
    if znachenie == 2:
        print(sluchai.get("2"))
        kvadrat(a=int(input("Enter the argument a: ")), b=int(input("Enter the argument b: ")),
                c=int(input("Enter the argument c: ")))
    if znachenie == 3:
        print(sluchai.get("3"))
        logar(a=int(input("Enter the argument  a: ")), b=int(input("Enter the argument b: ")))
    if znachenie == 0:
        print("Exit.")
        run=False
