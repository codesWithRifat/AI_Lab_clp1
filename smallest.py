""" Write a python program to find the
    smallest number from a set of numbers."""
num = [5, 9, 3, 8, 1]
small = num[0]
for i in num:
    if i < small:
        small = i

print("Smallest=", small)
