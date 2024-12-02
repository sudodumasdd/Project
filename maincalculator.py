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