import math 
cm = eval(input("Enter a height in CM: "))
Inches = cm / 2.54
print("The height in Inches is", Inches, "Inches")
Foot = Inches / 12
if Foot > 6 :
    print("Height is greater than 6ft")
else: 
    print("small boi")
Wholefeet = math.floor(Foot)
print(Wholefeet)
remainder = round(Inches - ( 12 * Wholefeet),2)
print("The Height is ", Wholefeet,"ft", remainder,"Inches")