a=10
b=0
try:
    d=a/b
    print(d)
    print("inside try")
except (NameError,ZeroDivisionError) as obj:
    print(obj)