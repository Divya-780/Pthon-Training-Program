first_name=tuple(input("Enter your first name:"))
last_name=tuple(input("Enter you last name:"))
#print(first_name)
#print(last_name)
name=first_name+last_name       #conctatenating two tuples
#print(name)
result=name[::-1]               #reversing the tuple items by using indexing
print(result)                   #printing name in the form of tuple