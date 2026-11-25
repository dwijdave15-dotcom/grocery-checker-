groceries = {"apple": 1, "milk": 2, "bread": 1.5, "eggs": 3}

def grocery_checker():

    while True:
        print("1. Show grocery items")
        print("2. Check price")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(groceries)

        elif choice == "2":
            item = input("Enter item: ")

            if item in groceries:
                print(groceries[item])
        
            else:
                print("Item not found")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

grocery_checker()
