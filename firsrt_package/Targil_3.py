number=int(input("enter number with three digits"))
num1=number%10
hhh=(number%100)%10
num2=int(((number%100)-hhh)/10)
num3=int((number-(number%100))/100)
print(f"{num1}{num2}{num3}")