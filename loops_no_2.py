#!/usr/bin/python3

# input from the letter
letter = input("Input: ").lower().strip()

# input from vowels 
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

for i in letter:
    if i not in vowels:
        print(i, end=", ")
    else:
        continue
