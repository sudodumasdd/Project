# This program implements a simple calculator that allows the user to perform 
# basic arithmetic operations: addition, subtraction, multiplication, and division.
# 
# The program works by presenting a menu of operations to the user, then 
# getting their choice and two numbers. It then performs the calculation based 
# on the chosen operation and prints the result.
# 
# The program includes error handling to prevent crashes due to invalid input 
# (such as letters instead of numbers) or division by zero.
# 
# The user can exit the calculator by choosing the "Exit" option from the menu.
# 
# Here's a breakdown of the code's main steps:
# 
# 1. Present a menu of operations: Add, Subtract, Multiply, Divide, Exit
# 2. Get the user's choice (1-5).
# 3. If the choice is 1-4:
#   - Get the first number.
#   - Get the second number.
# 4. Perform the calculation based on the choice:
#   - If choice is 1: Add the numbers.
#   - If choice is 2: Subtract the numbers.
#   - If choice is 3: Multiply the numbers.
#   - If choice is 4: Divide the numbers (checking for division by zero).
# 5. Print the result of the calculation.
# 6. If the choice is 5:
#   - Exit the program.
# 7. If the choice is invalid:
#   - Print an error message and repeat the process.

#Select operation
while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  #Gets your choice
  choice = input("Enter choice(1/2/3/4/5): ")
  #Checks if your choice is valid and gets your number
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue
    #The math part
    if choice == '1':
      print(num1, "+", num2, "=", num1 + num2)
    elif choice == '2':
      print(num1, "-", num2, "=", num1 - num2)
    elif choice == '3':
      print(num1, "*", num2, "=", num1 * num2)
    elif choice == '4':
      if num2 == 0:
        print("Division by zero error!")
      else:
        print(num1, "/", num2, "=", num1 / num2)
  #Exit command
  elif choice == '5':
    break
  else:
    print("Invalid input. Please enter a number between 1 and 5.")