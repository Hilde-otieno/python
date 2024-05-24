def add(a,b):
    answer = a + b
    return answer
def subtract(x, y):
    result = x - y
    return result
def multiply(c, d):
    result = c * d
    return result
def divide(m, n):
    division = m / n
    return division
def remainder(f, g):
    remain = f % g
    return remain
def power_of(s, t):
    power = s**t
    return power
def sum (*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
def multiplication(*integers):
    total = 1
    for integer in integers:
        total *= integer
    return total
def sum_and_greet(*args,**kwargs):
    total = 0
    for number in args:
        total+=number
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    greeting = f"Hello {first_name} {last_name}, the sum is {total}"
    return greeting
    # greeting = f"Hello{kwargs["first_name"]} {kwargs["last_name"]}, the sum of {list(args)} is {total}"
    # return greeting