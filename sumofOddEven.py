"""Write a python program to find the sum of
   odd and even numbers from a set of numbers."""
num = [1, 5, 3, 8, 9]
evenSum=0
oddSum=0
for i in (num):
    if(i%2==0):
        evenSum+=i
    else:
        oddSum+=i
print('Sum of Even numbers:', evenSum)
print('Sum of odd numbers:', oddSum)