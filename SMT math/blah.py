import random
A = int(input("Input an integer between 0-98: "))
B = int(input("Input an intger between 0-98: "))

def machine(A,B):
    sum = A + B
    return (sum % 99)
print(10 % 3)
values = []
start = machine(A,B)
for i in range(99):
    values.append(start)
    start = machine(start,start)
    
print(values)
