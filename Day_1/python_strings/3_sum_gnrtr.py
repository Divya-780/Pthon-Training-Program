'''Create a function digit_range_sum_gnrt that accepts two values (d, n) and does the following :
- prints numbers d dd ddd+ ... upto n as a list
- calculates sum of range d+dd+ddd+ ... upto n

ex. digit_range_sum_gnrt(5, 3)
[5, 55, 555]
615'''
#creating function that accepts two values
def digit_range_sum_gnrt(digit,n):
    s=0
    list_=[]
    #iterate the loop from 1 to that number
    for i in range(1,n+1):
        #converting digit into string and then integer and it will give repeated digits by multiplying the i for each iteration
        digit_repeated=int(str(digit)*i)
        #appending that repeated value to list
        list_.append(digit_repeated)
        #calculating the sum of all the items in the list
        s=s+digit_repeated
    print(list_)
    print(s)
digit = int(input())
n =int(input())
digit_range_sum_gnrt(digit,n)