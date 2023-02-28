from addition import addition
from division import div
from multiply import mult
from subtraction import subtract
from mod import mod
from percent import percent

a = int(input("Enter num 1 = "))
b = int(input("Enter num 2 = "))
op = input("Enter operation as symbol = ")

if(op == '+'): print("\nOutput = ",addition(a,b))
elif(op == '-'): print("\nOutput = ",subtract(a,b))
elif(op == '*'): print("\nOutput = ",mult(a,b))
elif(op == '/'): print("\nOutput = ",div(a,b))
elif(op == "%"): print("\nOutput = ",mod(a,b))
elif(op == "p"): print("\nOutput = ",percent(a,b))