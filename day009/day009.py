first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operator = input("enter operator: ")

if operator == '+':
    print(first_number + second_number)
if operator == '-':
    print(first_number - second_number)
if operator == '*':
    print(first_number * second_number)
if operator == '/':
    print(first_number / second_number)
else:
    print("Invalid operator")