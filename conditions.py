def print_numbers(n):
    numbers= range (n)
    for number in numbers:
        print(number)


def print_odd_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2!=0:
           print(number)

def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2==0:
            print(number)

def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number} is even")
        else:
            print(f"{number} is not even")

def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number} is divisible by 2")
        elif number%3==0:
            print(f"{number} is divisible by 3")
        elif number%5==0:
            print(f"{number} is divisible by 5")
        else:
            print(f"{number} is not divisble by 2,3 or 5")

def fizzbuzz(n):
    numbers = range(n)
    for number in numbers:
        if number%3==0:
             print("fizz")
        elif number%5==0:
             print("buzz")
        else: number%3!=0 and 5!=0
        print("fizzbuzz")

def countdown(n):
    while n>0:
        print(n)
        n-=1
        print(n)

def count_down(n):
    while n>0:
        print(n)
        if n==5:
            break
        n-=1

def divisible_by(n):
    x=0
    while x<=n:
        x+=1
        if x%7!=0:
            continue
        print(f"{x} is divisible by 7")

def combine(n):
    x= 0
    while x<=n:
        x+=1
        if x%2==0:
            continue
        print(x)

def mult(arr1, arr2):
    arr1= [2,3,4,5]
    arr2= [5,2,4,6]
    for i in arr1:
        if i

