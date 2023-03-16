#!/usr/bin/python3

# A python program that prints Weird for even numbers and odd numbers from the range of 6 to 21, and Not Weird for the rest
m = int(input("Enter a number: "))

if m % 2 == 0:
    print("Weird")
elif m % 2 != 0 and m in range(2, 6):
    print("Not Weird")
elif m % 2 != 0 and m in range(6, 21):
    print("Weird")
elif m % 2 != 0 and m > 20:
    print("Not Weird")
else:
    print("Invalid input, please enter a valid integer")

