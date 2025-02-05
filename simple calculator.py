print("Welcome to the Calculator!")

def calculator():
  
  print("Select operation:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  
  choice = input("Enter choice (1/2/3/4): ")
  # if choice >= '5' and choice == 0:
  #   print("Invalid input ")
  #   return calculator()
  
  num1 = float(int(input("Enter first number: ")))
  num2 = float(int(input("Enter second number: ")))
  
  if choice == '1':
    print(num1 + num2)
  elif choice == '2':
    print(num1 - num2)
  elif choice == '3':
    print(num1 * num2)
  elif choice == '4':
    print(num1 / num2)
  else:
    print("Invalid input")

  another_calculation = input('''Do you want to perform another calculation? (yes/no): ''')
  if another_calculation.lower() == 'yes':
     calculator()
  else: 
    print("Thank you for using the Calculator!")

calculator()