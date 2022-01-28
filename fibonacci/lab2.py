n=int(input("enter the numbers u want in this series"))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+second