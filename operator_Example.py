marks = 70
preksha_marks=80
# comparing 2 variables
ans=preksha_marks<=marks
# 80>70
print(ans)

#adding 10 marks in variable
preksha_marks*=0.5
ans=preksha_marks<=marks
print(f"{ans} - {preksha_marks}")

# logical operator (and,or,not)

a=10
b=20
ans=a>5 and a>b
print("This is logical operator ",ans)
ans=not(a>5 or a>b or b>10)
print("This is logical operator or ",ans)