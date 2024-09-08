a=int(input("enter first number :"))
b=int(input("enter second number :"))
sum = a+b

if (sum%7 == 0):
    print("divisible by 7")
else:
    print("not divisible by 7")
    
div_5= "divisible by 5" if sum%5==0 else "not divisble by 5"
print(div_5)
