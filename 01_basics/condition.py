
# if-else

age = 52
# age = int(input("Enter your age - ")) 

if(age >= 18):
    print("You are Eligible to Vote")
else: 
    print("You are not Eligible to vote")


# if-elif-else

value = 20
if(value == 0) :
    print("The value is 0")
elif(value < 0):
    print("The value is negative")
else:
    print("The Value is positive")


# ternary 
age1 = 10

#       value if true     condition       else       value if false
res = "Eligible to drive" if (age1 >= 20) else "Not Eligible to drive"
print(res)