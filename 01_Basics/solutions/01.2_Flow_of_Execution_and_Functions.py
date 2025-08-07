import math

# 1. Euclidean Distance
def euclidean_distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean distance between two Cartesian coordinates.
    
    Parameters:
    x1, y1 -- coordinates of the first point
    x2, y2 -- coordinates of the second point
    
    Returns:
    float -- the distance between the two points
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# 2. Converters

def cm_to_inches(cm):
    """
    Converts centimeters to inches.
    
    Parameters:
    cm (float): Measurement in centimeters
    
    Returns:
    float: Measurement in inches
    """
    return cm / 2.54

def kg_to_pounds(kg):
    """
    Converts kilograms to pounds.
    
    Parameters:
    kg (float): Weight in kilograms
    
    Returns:
    float: Weight in pounds
    """
    return kg / 0.45359


# 3. Foreign Exchange

def convert_to_aud(usd_amount, exchange_rate=1.34):
    """
    Converts USD to AUD using a default or provided exchange rate.
    
    Parameters:
    usd_amount (float): Amount in US dollars
    exchange_rate (float, optional): Conversion rate (default is 1.34)
    
    Returns:
    float: Equivalent amount in Australian dollars
    """
    return usd_amount * exchange_rate


# 4. Body Mass Index

def get_bmi(weight_kg, height_m):
    """
    Calculates Body Mass Index (BMI).
    
    Parameters:
    weight_kg (float): Weight in kilograms
    height_m (float): Height in meters
    
    Returns:
    float: BMI value
    """
    return weight_kg / (height_m ** 2)


# 5. Check My Number

def is_even(n):
    """
    Checks if a number is even.
    
    Parameters:
    n (int): The number to check
    
    Returns:
    bool: True if even, False otherwise
    """
    return n % 2 == 0

def is_divisible(x, y):
    """
    Checks if x is divisible by y.
    
    Parameters:
    x (int): Dividend
    y (int): Divisor
    
    Returns:
    bool: True if divisible, False otherwise
    """
    return x % y == 0


# 6. Heron's Formula

def heron_area(a, b, c):
    """
    Calculates the area of a triangle using Heron's formula.
    
    Parameters:
    a, b, c (float): Lengths of the sides of the triangle
    
    Returns:
    float: Area of the triangle
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_from_square_areas(A, B, C):
    """
    Calculates triangle area given the areas of three squares (adjacent to triangle sides).
    
    Parameters:
    A, B, C (float): Areas of the squares on the triangle's sides
    
    Returns:
    float: Area of the triangle
    """
    a = math.sqrt(A)
    b = math.sqrt(B)
    c = math.sqrt(C)
    return heron_area(a, b, c)


# --------------------
# Example Test Calls
# --------------------

# Task 1
print("Distance between (0, 0) and (3, 4):", euclidean_distance(0, 0, 3, 4))

# Task 2
print("1.0 cm is", round(cm_to_inches(1.0), 2), "inches")
print("1.0 kg is", round(kg_to_pounds(1.0), 5), "pounds")

# Task 3
print("USD $1 to AUD (default):", convert_to_aud(1))
print("USD $1 to AUD (custom rate):", convert_to_aud(1, 1.37))
print("USD $5000 to AUD:", convert_to_aud(5000))

# Task 4
print("BMI (75kg, 1.75m):", get_bmi(75, 1.75))
print("BMI (120kg, 1.75m):", get_bmi(120, 1.75))

# Task 5
print("Is 10 even?", is_even(10))
print("Is 15 divisible by 5?", is_divisible(15, 5))
print("Is 14 divisible by 3?", is_divisible(14, 3))

# Task 6
print("Triangle area from square areas A=370, B=116, C=74:", area_from_square_areas(370, 116, 74))