"""Write a python program to find the largest
   number between two numbers using function"""


def find_large(a, b):
    if a > b:
        return a
    else:
        return b


print("Largest number:", find_large(45, 76))
