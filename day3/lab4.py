# Given three integers, print the smallest one. (Three integers should be user input) 
a=int(input("enter first integer"))
b = int(input("enter 2nd integer"))
c = int(input("enter 3rd integer"))
if(a<=b and a<=b):   #Compare the first number with the second and third number
  print(a," is the smallest")
elif(b<=a and b<=c):#Compare the second number with the first and third number
  print(b," is the smallest")
else:
    print(c," is the smallest")