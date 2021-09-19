#count the number occurrence of a specific character in a string.
s=input("enter the string:")
spec_char=input("Enter the the char u want to count:")
count_=0
for char in s:   #iterate the entire string 
    if(spec_char==char): #every time checking the whether the spec char is present or not..if it is present then enter into if block
        count_+=1         #increment the count
print(count_)   