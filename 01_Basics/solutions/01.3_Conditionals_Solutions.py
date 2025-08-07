# 1. What shape is it?
def determine_shape():
    sides = int(input("How many sides does the shape have? "))
    
    if sides == 0:
        print("Circle")
    elif sides == 3:
        print("Triangle")
    elif sides == 4:
        equal = input("Are all the sides equal? [Yes/No] ").strip().lower()
        if equal == "yes":
            print("Square")
        else:
            print("Rectangle")
    else:
        print("Shape not recognised")

# 2. Is it raining?
def should_take_transport():
    raining = input("Is it currently raining? ").strip().lower()
    
    if raining == "yes":
        print("You should take the bus.")
    else:
        distance = int(input("How far in km do you need to travel? "))
        if distance > 10:
            print("You should take the bus.")
        elif distance >= 2:
            print("You should ride your bike.")
        else:
            print("You should walk.")

# 3. Minimum and Maximum
def builtin_minmax():
    a = int(input("Enter 1st integer: "))
    b = int(input("Enter 2nd integer: "))
    c = int(input("Enter 3rd integer: "))
    
    print("Min:", min(a, b, c))
    print("Max:", max(a, b, c))

def minimum(x, y):
    return x if x < y else y

def maximum(x, y):
    return x if x > y else y

def minmax(x, y, which):
    if which == "min":
        return minimum(x, y)
    elif which == "max":
        return maximum(x, y)
    else:
        raise ValueError("Parameter must be 'min' or 'max'")

# 4. Shout
def shout(text):
    upper = text.upper()
    if not upper.endswith("!"):
        upper += "!"
    return upper


# Uncomment the following to test specific tasks:
# determine_shape()
# should_take_transport()
# builtin_minmax()
# print(minimum(3, 5))
# print(maximum(3, 5))
# print(minmax(10, -2, "min"))
# print(shout("hello"))
# print(shout("hello!"))