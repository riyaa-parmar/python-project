from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            with open(self.filename, "a") as file:
                entry = input("Enter your journal entry:\n")
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                file.write(f"{timestamp}\n{entry}\n\n")
                print("Entry added successfully!\n")
        except Exception as e:
            print("Error while writing entry:", e)

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                if content.strip() == "":
                    print("No journal entries found.\n")
                else:
                    print("\nYour Journal Entries:")
                    print(content)
        except FileNotFoundError:
            print("Journal file does not exist. Please add a new entry first.\n")

    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")
            with open(self.filename, "r") as file:
                lines = file.readlines()
                found = False
                for line in lines:
                    if keyword in line:
                        print(line.strip())
                        found = True
                if not found:
                    print("No entries found for the given keyword.\n")
        except FileNotFoundError:
            print("Journal file does not exist.\n")

    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            with open(self.filename, "w") as file:
                pass
            print("All journal entries have been deleted.\n")
        else:
            print("Delete operation cancelled.\n")

def menu():
    journal = JournalManager()

    print("Welcome to Personal Journal Manager!")
    while True:
        print("""
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            journal.add_entry()
        elif choice == "2":
            journal.view_entries()
        elif choice == "3":
            journal.search_entry()
        elif choice == "4":
            journal.delete_entries()
        elif choice == "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

menu()