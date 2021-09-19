all_digit_list=[0,1,2,3,4,5,6,7,8,9]
n=int(input("enter number:"))
#creating empty set for missing numbers
missing_elements=set()
#convert that number into string 
res=list(map(int,str(n)))
sorted(res)
for ele in all_digit_list:
    #member check function
    if ele not in res:
        missing_elements.add(ele)
#set(missing_elements)
print(missing_elements)