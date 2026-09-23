# (program to find the area of a circle)

def circle_area(radius):
    area = 3.14 * radius * radius
    return area
  
radius = float(input("Enter the radius: "))

result = circle_area(radius)
print("Area of the circle =", result)


# (Program to find the largest of three numbers)

def largest_number(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = largest_number(num1, num2, num3)
print("Largest number =", largest)


# (program to find a string length without using built-in length function)

def string_length(text):
    count = 0

    for character in text:
        count = count + 1
    return count

text = input("Enter a string: ")

length = string_length(text)
print("Length of the string =", length)


# (Program to check whether a number is prime)

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# (Program to find nth Fibonacci number)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
      
n = int(input("Enter the position: "))
result = fibonacci(n)

print("Fibonacci number =", result)


# (Program to reverse a string)

def reverse_string(text):
    if text == "":
        return text
    else:
        return reverse_string(text[1:]) + text[0]

text = input("Enter a string: ")
result = reverse_string(text)

print("Reversed string =", result)


# (Program to Sum of all numbers from 1 to n using for loop)

n = int(input("Enter the value of n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum from 1 to", n, "=", total)


# (Program to count how many even numbers)

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    number = int(input("Enter number: "))
    numbers.append(number)

count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print("Number of even numbers =", count)


# (Program to print all prime numbers between 1 and 100)

for number in range(2, 101):

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
