# Write a python program to generate Fibonacci series.
n=10
a=0
b=1
print("Fibonacci series till", n, "term:")
print(a, "+", b, end=" ")
temp=a+b
for i in range(n-2):
    temp=a+b
    a=b
    b=temp
    print("+", temp, end=" ")