#Write a program to compute the distance between the points (x1, y1) and (x2, y2)
import math
x1=int(input("enter x1:"))
x2=int(input("enter x2:"))
y1=int(input("enter y1:"))
y2=int(input("enter y2:"))
#distance calc by using ecludian method
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)