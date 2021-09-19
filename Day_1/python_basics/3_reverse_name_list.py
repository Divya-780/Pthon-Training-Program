#Prompt user for first, last names and print them in reverse order
first_name=list(input("Enter your first name:"))
last_name=list(input("Enter you last name:"))
#print(first_name)
#rint(last_name)
first_name.extend(last_name) #extending last_name to first_name
#print(first_name)
rev_list=first_name[::-1] #reversing list elements by using indexing
print(rev_list)