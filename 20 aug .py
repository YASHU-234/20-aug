def cal():
    while True:
        n = input( "\nSelect operation:\n""1. Addition\n""2. Subtraction\n""3. Multiplication\n""4. Division\n""5. Power\n""6. Cube\n""7. Exit\n""Enter choice: ")
        if n == "1" or n.lower() == "addition":
            print(int(input("Number 1: ")) + int(input("Number 2: ")))
        elif n == "2" or n.lower() == "subtraction":
            print(int(input("Number 1: ")) - int(input("Number 2: ")))
        elif n == "3" or n.lower() == "multiplication":
            print(int(input("Number 1: ")) * int(input("Number 2: ")))
        elif n == "4" or n.lower() == "division":
            n1 = int(input("Number 1: "))
            n2 = int(input("Number 2: "))
            print(n1 / n2 if n2 != 0 else "Error: Division by zero")
        elif n == "5" or n.lower() == "power":
            base = int(input("Base: "))
            exp = int(input("Exponent: "))
            print(base ** exp)
        elif n == "6" or n.lower() == "cube":
            print(int(input("Number: ")) ** 3)
        elif n == "7" or n.lower() == "exit":
            print("Exiting calculator... Goodbye!")
            break
        else:
            print("Invalid input. Try again.")



def login_system():
    correct_password = "python123"  
    attempts = 3
    while attempts > 0:
        password = input("Enter password: ")
        if password == correct_password:
            print("Login successfully")
            return
        else:
            attempts -= 1
            print(f"Incorrect password. Attempts left: {attempts}")
    print("Too many failed attempts. Access denied ")


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)




