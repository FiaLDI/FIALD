# We define a function that calculates all the divisors of a number and returns a list
def delet(x):
    lst = [1, x]
    for i in range(2, 1 + int(x ** 0.5)):
        if x % i == 0:
            lst.extend({x // i, i})
    return sorted(lst)


x = int(input("Enter the first number: "))
y = int(input("Enter the second number : "))
print("First number divisors  -",delet(x))
print("Second number divisors  -",delet(y))


# Create a function that creates a set from the resulting lists and calculates their intersection
def obp(x, y):
    a = set(delet(x))
    b = set(delet(y))
    c = b.intersection(a)
    return c


print("Common divisors -",obp(x, y))
