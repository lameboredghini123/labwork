# WAP which accepts marks of four subjects and display total marks, 
# percentage and grade. Hint: more than 70% –> distinction, 
# more than 60% –> first, more than 40% –> pass, less than 40% –> fail 

sub1=int(input("enter your marks of subject 1"))
sub2=int(input("enter your marks of subject 2"))
sub3=int(input("enter your marks of subject 3"))
sub4=int(input("enter your marks of subject 4"))
total_marks=sub1+sub2+sub3+sub4
total_percentage=total_marks%400*100
print("you scored",total_percentage)
if total_percentage>=70:
    print("distinction")
elif total_percentage>=60:
    print("first")
elif total_percentage>=40:
    print("pass")
elif total_percentage<40:
    print("fail")