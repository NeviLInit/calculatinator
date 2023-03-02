from addition import addition
from division import div
from multiply import mult
from subtraction import subtract
from mod import mod
from percent import percent
from log import lo
from sqrt import sq

print("\nCALCULATOR\n\nMenu : \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Percentage\n7. Log Function\n8. Square Root")
ch = int(input("Enter Your Choice : "))

if(ch < 7 and ch > 0):
    a = int(input("Enter num 1 = "))
    b = int(input("Enter num 2 = "))
elif(ch > 6 and ch < 9 ):
    a = int(input("Enter num = "))

if(ch == 1): print("\nOutput = ",addition(a,b))
elif(ch == 2): print("\nOutput = ",subtract(a,b))
elif(ch == 3): print("\nOutput = ",mult(a,b))
elif(ch == 4): print("\nOutput = ",div(a,b))
elif(ch == 5): print("\nOutput = ",mod(a,b))
elif(ch == 6): print("\nOutput = ",percent(a,b),"%")
elif(ch == 7): print("\nOutput = ",lo(a))
elif(ch == 8): print("\nOutput = ",sq(a))
else: print("\nInvalid Input")

