import math

def math_menu():
    while True:
                print("\nMathematical operations:")
                print("Enter 1 to calculate factorial!")
                print("Enter 2 to solved compound interest!")
                print("Enter 0 for go to the main menu!\n")

                try:
                    mchoice = int(input("Enter your choice: "))
                except Exception:
                    print("Invalid ianput!")
                    continue

                if mchoice == 1:

                    num = int(input("Enter number for calculate factorial: "))
                    fact= math.factorial(num)
                    print(f"factorial of {num} is: {fact}")

                elif mchoice == 2:
                    p = float(input("Enter principal amount: "))
                    r = float(input("Enter rate of interest (%): "))
                    t = float(input("Enter time (years): "))
                    ci = p * (1 + r/100) ** t
                    print("Compound Interest:", round(ci, 2))

                elif mchoice == 0:
                    break

                else:
                    print("Invalid choice!")