while True:
print("Welcome to the Pattern Generator and Number Analyzer!")
    print("select an opption")
    print("1. Right-angled Triangle")
    print("2. Pyramid Pattern")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            print("Invalid row count!")
            break
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()
    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            print("Invalid row count!")
            break
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end="")
            for space in range(2 * i - 1):
                print("*", end="")
            print()
    elif choice == "3":
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            print("Invalid row count!")
            break
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end="")
            for space in range(i):
                print("*", end="")
            print()
    elif choice == "4":
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        if start > end:
            print("Error! End number must be greater than start number.")
            continue
        total = 0
        print("\nOdd/Even Analysis:")
        for num in range(start, end + 1):
            if num == 0:
                pass
 if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")
            total += num
        print("Sum of all numbers =", total)
    elif choice == "5":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid choice! Please try again.")
        


        
        

