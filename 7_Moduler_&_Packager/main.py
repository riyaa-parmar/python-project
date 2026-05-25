import modules

def main_menu():
    while True:
        print("\nWelcome to my multi-utility toolkit")
        print("Choose an option:")
        print("Enter 1 for Datetime and time operations!")
        print("Enter 2 for Mathematical Operations!")
        print("Enter 3 for Random data generation!")
        print("Enter 4 for Generate Unique Identifiers!")
        print("Enter 5 for File operations!")
        print("Enter 6 for Explore module attributes!")
        print("Enter 0 for exit!\n")
    
        try:
            choice = int(input("Enter your choice: "))
        except Exception:
            print("Invalid ianput!")
            continue

        if choice == 1:
            modules.datetime_menu()

        elif choice == 2:
            modules.math_menu()

        elif choice == 3:
            modules.random_menu()

        elif choice == 4:
            modules.uuid_menu()

        elif choice == 5:
            modules.file_menu()

        elif choice == 6:
            modules.explore_menu()

        elif choice == 0:
            print("Thank you for using the toolkit!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()