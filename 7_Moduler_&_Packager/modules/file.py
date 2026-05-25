import os

def file_menu():
    while True:
            print("\nFile Operations:")
            print("Enter 1 to create a new file!")
            print("Enter 2 for write in file!")
            print("Enter 3 for read from file!")
            print("Enter 4 for append to a file!")
            print("Enter 5 for delete file!")
            print("Enter 0 for go to the main menu!\n")

            try:
                fchoice = int(input("Enter your choice: "))
            except Exception:
                print("Invalid ianput!")
                continue

            if fchoice == 1:
                name = input("Enter file name: ")
                open(name, "w").close()
                print("File created successfully")

            elif fchoice == 2:
                name = input("Enter file name: ")
                data = input("Enter data: ")
                with open(name, "w") as f:
                    f.write(data)
                print("Data written successfully")

            elif fchoice == 3:
                name = input("Enter file name: ")
                with open(name) as f:
                    print("File Content:\n", f.read())

            elif fchoice == 4:
                name = input("Enter file name: ")
                data = input("Enter data: ")
                with open(name, "a") as f:
                    f.write("\n" + data)
                print("Data appended successfully")

            elif fchoice == 5:
                name = input("Enter file name to delete: ")

                if os.path.exists(name):
                    os.remove(name)
                    print("File deleted successfully")
                else:
                    print("File does not exist")

            elif fchoice == 0:
                break

            else:
                    print("Invalid choice!")