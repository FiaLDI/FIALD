# A program that creates sets and performs some operations on them


# Create a list using the input method
def setlist(a):
    '''Enters numbers into the list,
in order to complete the input -
write any character other than a digit '''
    try:
        print("Enter list numbers ")
        while True:
            x = int(input("Input: "))
            a.append(x)
    except:
        print("List created :", a)


# Function (&) - Computing the intersection of sets
def intersept(a, b):
    d = set(a)
    c = set(b)
    ar = d.intersection(c)
    print(ar)


# Function (|) - Computing union of sets
def unio(a, b):
    d = set(a)
    c = set(b)
    ar = d.union(c)
    print(ar)


# Function (-) - Computing not union of sets
def diiffer(a, b):
    d = set(a)
    c = set(b)
    ar = d.difference(c)
    print(ar)


# Еmpty lists
b = []
c = []


# The loop that runs the program
# Turns lists into sets
# Does operations with them:
# intersection, union, difference
run = False
start = str(input("Start the program with the (start) command  - "))
if start == "старт" or start == "start":
    run = True
    print("Starts up...")
    print(setlist.__doc__)
while run:
    setlist(b)
    setlist(c)
    usl = input("Enter operation - [& , |, -] - ")
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