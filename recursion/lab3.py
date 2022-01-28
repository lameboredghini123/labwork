def factorial(num): 
    if num<0:
        return "number cannot be negative"
    elif num==1 or num==0:
        return 1
    else:
        result=num*factorial(num-1)
        return result
print(factorial(5))