a=10
b=0
try:
    d=a/b
    print(d)
    print("Inside try")
except ZeroDivisionError:
    print("division by zero isnt allowed")
else:
    print("inside else")