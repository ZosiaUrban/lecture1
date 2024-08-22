intVariable = 4
floatVariable=4.5
StringVariable= "Hello Pookie"
print(intVariable)
print(floatVariable)
print(StringVariable)

print(type(floatVariable))

intVariable= int(floatVariable)
#type casting variable value will be 4 because it only takes intiger value
print(intVariable)

print("here is my greeting", StringVariable)
''''
hello the computer is ignoring these lines 

'''''

shareOfLoan= 500.50/3
print(shareOfLoan)
print(int(shareOfLoan))
#prints in non decimal way

num1 = int(input("Enter a number"))
# asls user for inout
print(num1)
num2= int(input("Enter another number"))
print(num2)
#you have to add the type before the input for mathematical calculations
sum= num1 + num2
print(sum)
sum=sum * 2
print(sum)

name=input("Enter your name")
school=input("Enter your school")
print("your name is",name)

print(f"your name is, {name}, and your shcool is: {school}")

# if you want to add teo decimal places in float you write floatVariable:.2f