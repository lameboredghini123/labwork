#WAP to calculate & print the area of a triangle
#area of triangle=1/2*base*height

#asking the user to input the base and height values and storing them in variables 'base' and 'height'
base=int(input("enter the base value of the triangle in cm"))
height=int(input("enter the height value of the triangle in cm"))

#calculating the area of triangle and storing this value in the variable 'area_triangle'
area_triangle=1/2*base*height

print("the area of the triangle is",area_triangle,"cm\u00b2")   #cm\u00b2 is used to print the cm squared value,2=square,3=cube