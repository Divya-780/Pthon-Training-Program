#Split the following string into a list using the separator and print the first, last elements

#Red-Orange-Green-Blue
s=input("Enter string separated by hyphen:")
list_=list(s.split("-"))   #split the list by using "-"
print(list_[0],list_[-1])  #printing last and 1st ele by using indexing

