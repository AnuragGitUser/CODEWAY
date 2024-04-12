print("Simple Calculator using Python")
print("Enter two numbers: ")
a = float(input("1st no.: "))
b = float(input("2nd no.: "))
print("Operation choice: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
c = int(input("Enter choice no.: "))

if c == 1:
    print("The addition of " + str(a) + " & " + str(b) + " is", a + b)
elif c == 2:
    print("The subtraction of " + str(a) + " & " + str(b) + " is", a - b)
elif c == 3:
    print("The multiplication of " + str(a) + " & " + str(b) + " is", a * b)
elif c == 4:
    print("The division of " + str(a) + " & " + str(b) + " is", a / b)
else:
    print("Invalid choice")


