# py program for simple calculator 

# func to +,-,*,/
def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2 

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2 

print("Please select operation - \n " \
	"1. Add \n "
	"2. subtract \n"
	"3. multiply \n"
	"4. divide   \n")


# input 
select = int(input("Please select operation form 1,2,3,4 : "))

num_1 = int(input("Enter first num: "))
num_2 = int(input("Enter second num: "))


if select == 1:
	print(num_1, "+", num_2, "=",
		add(num_1, num_2))

elif select ==2 : 
	print(num_1, "-", num_2, "=",
		subtract(num1, num_2))

elif select == 3 :
	print(num_1, "*", num_2, "=",
		subtract(num_1, num_2)) 

elif select == 4 : 
	print(num_2, "/", num_2, "=",
		divide(num_1, num_2))
else: 
	print("Invalid input")

























