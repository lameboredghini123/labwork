try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a/b;
    print(c)
except:
    print("can't divide by zero")
else:
    print("hi im else block")