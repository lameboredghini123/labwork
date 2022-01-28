''' Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample: list1 = [‘aba’,’121’,’kgf’,’abc’] '''

s=0
list = ['aba','121','kgf','abc']
for x in list:
    if len(x)>1 and x[0]==x[-1]:
        print("the given words are: ", x )
        s=s+1
    print("no. of words you want ", s )