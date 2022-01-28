def add_series(num):    #1.defining the parameter
    if num==1: 
        return 1
    else:
        return num+add_series(num-1)
n=int(input("enter a real postive integer"))    #3. asking the user for a value, this value gets stored in 'n' and also in 'num' after the function has been called
ans=add_series(n)   #2.calling the function and defining its value and storing it in the variable 'ans'
print(f"the sum from 1 to {n} is {ans}")