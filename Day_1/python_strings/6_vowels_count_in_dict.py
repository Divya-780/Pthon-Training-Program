#For a given string, print the count of different vowels in it.

#taking input string from the user
s=input("Enter the string:")
#convert all the characers in a string into small letters by using casefold function
s=s.casefold()
#initialize the variable for counting vowels
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
#iteratre string up to end by using for loop
for ele in s:
    #check if the ele in string is vowel or not..if it is vowel then increment corresponding vowel count and then print
    if ele=="a":
        a_count+=1
    elif ele=="e":
        e_count+=1
    elif ele=="i":
        i_count+=1
    elif ele=="o":
        o_count+=1
    elif ele=="u":
        u_count+=1
print("a-",a_count)
print("e-",e_count)
print("i-",i_count)
print("o-",o_count)
print("u-",u_count)