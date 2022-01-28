#reverse the string using loop

def reverse(s): 
    str=""
    for i in s:
        str=i+str
    return str
s="programming"
print("the original string is ",end="")
print(s)
print("the reversed string using loop is ",end="")
print(reverse(s))