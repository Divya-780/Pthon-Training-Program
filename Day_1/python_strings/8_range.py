a=int(input("enter 1st value:"))
b=int(input("enter second value:"))
n=int(input("enter the number:"))
variance=abs((b-a)/a*100) #after calc the variance convert valu into poisitive by using abs
#print(variance)
if(n<variance):
    print("Number is within variance of range limits")
else:
    print("Number is without variance of range limits")
