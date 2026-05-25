import datetime
import time

def datetime_menu():
    while True:
            print("\ndate and tiem operations:")
            print("Enter 1 to dispaly current date and time!")
            print("Enter 2 to Calculates the difference between two dates!")
            print("Enter 3 to Format date into custom format!")
            print("Enter 4 for stpowatch!")
            print("Enter 0 for go to main menu!\n")

            try: 
                dchoice = int(input("Enter your choice: "))
            except Exception:
                print("Invalid ianput!")
                continue

            if dchoice == 1:
                now = datetime.datetime.now()
                print("Current Date & Time:", now)

            elif dchoice == 2:
                d1 = input("Enter first date (YYYY-MM-DD): ")
                d2 = input("Enter second date (YYYY-MM-DD): ")

                d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

                diff = abs(d2 - d1)
                print("Difference:", diff)

            elif dchoice == 3:
                d = input("Enter date (YYYY-MM-DD): ")
                d = datetime.datetime.strptime(d, "%Y-%m-%d")
                print("Formatted Date:", d.strftime("%d-%m-%Y"))

            elif dchoice == 4:
                input("Press Enter to start stopwatch")
                start = time.time()
                input("Press Enter to stop stopwatch")
                print("Time:", round(time.time() - start, 2), "seconds")

            elif dchoice == 0:
                break
        
            else:
                print("Invalid choice!")