#a school decided to replace desks in three classrooms. Each desk sits two students. Given the number of students
#in each class, print the smallest number of desks that can be be purchased. The program should read three integers
#the number of students in each class a, b, and c respectively. 

a=int(input("enter the number of students in the first classroom"))
b=int(input("enter the number of students in the second class"))
c=int(input("enter the number of students in the third class"))

table1 = (class1 // 2 + class2 // 2 + class3 // 2)
table2=  (class1 % 2 + class2 % 2 + class3 % 2)
print("So,we need {} desks in total".format(table1+table2))