#take input string from user
s=input("Enter the string:")
s=s.casefold()
list_1=[]
list_2=[]
result=[]
#check if the string starts with is or not
if s.startswith("is"):
    print(s)
#if the string is not starts with is.then add
else:
    list_1=list(s)
    list_2.append("Is ")
    result=list_2+list_1
   # print(result)
    
new_string=''.join(str(ele) for ele in result)
print(new_string)