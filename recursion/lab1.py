def factorial_recursive(n,i):
    if i>10:
        return 1
    print(n,"*",i,"=",n*i)
    return factorial_recursive(n,i+1)
    n=8
factorial_recursive(n,1)