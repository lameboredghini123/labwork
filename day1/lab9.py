#WAP to calculate and print the sum of positive odd integers until 10
#declaring the sum of odd numbers in the range as zero and storing it in the variable 'oddtotal'
odd_total=0
#declaring the range
for num in range(1,11):
#stating a condition 
    if num%2!=0:
        print("{0}".format(num))
        odd_total = odd_total+num
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(num,odd_total)) 