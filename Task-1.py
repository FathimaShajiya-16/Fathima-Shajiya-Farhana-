# (Program to find the largest of three numbers)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x == y == z:
    print("All three numbers are equal")

elif x == y:
    if x > z:
        print("First and second numbers are equal and largest")
    else:
        print("Third number is largest")

elif y == z:
    if y > x:
        print("Second and third numbers are equal and largest")
    else:
        print("First number is largest")

elif x == z:
    if x > y:
        print("First and third numbers are equal and largest")
    else:
        print("Second number is largest")

elif x > y and x > z:
    print("First number is largest")

elif y > x and y > z:
    print("Second number is largest")

else:
    print("Third number is largest")



# (Program to check whether a given year is a leap year or not)

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("The given year is a leap year")

elif year % 100 == 0:
    print("The given year is not a leap year")

elif year % 4 == 0:
    print("The given year is a leap year")

else:
    print("The given year is not a leap year")



# (Program to check whether a character is a vowel or consonant)

character = input("Enter a character: ")

if len(character) != 1:
    print("Please enter only one character")

elif character.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("The given character is a vowel")

elif character.isalpha():
    print("The given character is a consonant")


# (Program to check whether a number is divisible by both 5 and 11)

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11")

else:
    print("The number is not divisible by both 5 and 11")


# (Program to calculate the sum of first N natural numbers using a while loop)

n = int(input("Enter a number: "))
i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1
print("Sum of first", n, "natural numbers is:", total)


# (Program to print the multiplication table of a given number using a while loop)

number = int(input("Enter a number: "))

i = 1

while i <= 10:
    result = number * i
    print(number, "x", i, "=", result)
    i = i + 1


# (Program to print a pyramid pattern)

number_of_rows = int(input("Enter the number of rows: "))

for i in range(1, number_of_rows + 1):
    spaces = number_of_rows - i
    stars = (2 * i) - 1
    print(" " * spaces + "*" * stars)


# (Program to print a number pattern)

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



