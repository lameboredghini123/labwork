#N students take K apples and distribute them among each other evenly. The remaining
#(the indivisible part) remains in the basket. How many apples will each student get?
#how many apples will remain in the basket? The program reads the numbers N and K
#It should print the two answers for the questions above.

N=int(input("enter the number of students"))
K=int(input("enter the number of apples"))

apples_each_student=K//N

apples_basket=K%N

print("each student will get",apples_each_student,"apples")
print("the number of apples remaining in the basket will be",apples_basket)