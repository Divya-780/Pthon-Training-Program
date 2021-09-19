#For a given string, print the count of vowels and consonants.
#Taking input from the user
s=input("Enter string:")
#counting vowels 
vow_count=0
#for consonants count
cons_count=0
#put all the vowles in a list called vowel
vowels=['A','E','I','O','U','a','e','i','o','u']
consonants=['B','b','C','c','D','d','F','f','G','g','J','j','K','k','L','l','M','m','N','n','P','p','Q','q','S','s','T','t','V','v','X','x','Z','z','R','r','W','w','Y','y']
#iterate until end of the string
for ele in s:
    #check if the ele in string is in vowels list 
    if ele in vowels:
        vow_count=vow_count+1
    #if(ele=="#" or ele=="+" ele=="&"):
    if ele in consonants:
        cons_count+=1
print(vow_count)
print(cons_count)
