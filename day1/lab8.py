#WAP to calculate & print the sum of positive even integers until 10

#here we are declaring a range that starts with 1 and ends with 11, and has intervals of 2, as 2 
num=range(1,11,2)

#using the sum() function to find the sum of the range
sum_range=sum(num)

#printing the sum of the range
print("the sum of positive even integers until 10 is",sum_range)
