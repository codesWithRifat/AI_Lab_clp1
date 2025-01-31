""" Write a python program to find the second
    highest number from a set of numbers."""
num = [5, 9, 3, 8, 1]
max = num[0]
for i in num:
    if i > max:
        max = i
max2 = num[0]
for i in num:
    if i > max2 and i < max:
        max2 = i
print("Second highest number is", max2)