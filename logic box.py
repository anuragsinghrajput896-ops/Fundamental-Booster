print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == 2:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        total = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")
            total += num
        print("Sum of numbers from", start, "to", end, "is:", total)

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
