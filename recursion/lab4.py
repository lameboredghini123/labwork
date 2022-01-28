#base condition example

def func1(n):
    if n==0:
        print("finally")
    else:
        print(n)
        func1(n-3)
func1(15)