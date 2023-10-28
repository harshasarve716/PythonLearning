# condition
# set of rules

score = int(input("enter the marks\n"))
print(score)
if score > 90 and score<80:
    print("grade A")
elif score > 70 and score<60:
    print("grade B")
elif score > 50 and score <40:
    print("garde C")
else:
    print("fail")
