def sum_d(n):
    if(n==0):
       return 0
    else:
        r=n%10
    return(r + sum_d(n//10))
n=int(input("Enter a number: "))
print(sum_d(n))