#Given an integer N - the number of minutes passed since midnight(0:00) - 
#WAP to find & print the hours and minutes displayed on the 24 hour clock

N=int(input("enter the number of minutes that have passed since midnight"))
num_of_hours=N//60
num_of_minutes=N%60
print("the time displayed on the 24 hour clock is",num_of_hours,":",num_of_minutes)