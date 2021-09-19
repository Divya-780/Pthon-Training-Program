'''Prompt user to enter a value and then print value's content type (alpha, numeric, alphanumeric).

Note: Program shall continuously prompt user to enter value until "exit" is entered.'''
#iterate over loop untill exit is enter
while(True):
   #Prompt user to enter a value and then print value's content type (alpha, numeric, alphanumeric).
   #Note: Program shall continuously prompt user to enter value until "exit" is entered.
   n=input("enter any values:")
   #if input is equal to exit then break the loop
   if(m=="exit"):
      break
   #if input is not exit then iterate loop print type
   elif(m.isalpha()):
      print("alpha")
   elif(m.isnumeric()):
      print("numeric")
   elif(m.isalnum()):
      print("alphanumeric")