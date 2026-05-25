import random

def random_menu():
    while True:
            print("\nRandom data generation:")
            print("Enter 1 to Generate random number!")
            print("Enter 2 to Generate random list!")
            print("Enter 3 to Create random password!")
            print("Enter 4 to Generate random OTP")
            print("Enter 0 for go to the main menu!\n")

            try:
                rchoice = int(input("Enter your choice: "))
            except Exception:
                    print("Invalid ianput!")
                    continue

            if rchoice == 1:
                print("Random Number:", random.randint(1, 1000))

            elif rchoice == 2:
                print("Random List:", [random.randint(1, 1000) for _ in range(5)])

            elif rchoice == 3:
                length = int(input("Enter password length: "))
                chars = "0123456789"
                pwd = "".join(random.choice(chars) for _ in range(length))
                print("Generated Password:", pwd)

            elif rchoice == 4:
             print("OTP:", random.randint(1000, 9999))

            elif rchoice == 0:
                break

            else:
                print("Invalid choice!")
