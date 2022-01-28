try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a/b;
    print(c)
except Exception as e:
        print(e)
else:
    print("hi im else block")
