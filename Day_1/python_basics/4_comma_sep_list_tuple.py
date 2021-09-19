#Prompt user to enter a sequence of comma-separated numbers and generate a list and a tuple with those numbers
comma_sep_values=input("plz enter comma separated numbers:")
list_=list(comma_sep_values.split(",")) #separating list by using split function
#print(type(list_))
print(list_)
tup = tuple(comma_sep_values.split(","))  #converting list to tuple
print(tup)
#print(type(tup))