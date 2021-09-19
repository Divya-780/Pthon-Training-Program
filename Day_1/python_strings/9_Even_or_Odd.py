'''Prompt user to enter a number and then print out message if it is odd or even.'''
n=int(input("Enter the number:"))
#modulus operator
if(n%2==0):
    print("Even")
else:
    print("odd")