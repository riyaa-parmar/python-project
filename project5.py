class Employee:
    def __init__(self, name="", age=0, emp_id=0, salary=0):
        self.name = name
        self.age = age
        self.__employee_id = emp_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print(self.name, self.age, self.__employee_id, self.__salary)

    def __del__(self):
        print("Employee object destroyed")

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language:", self.language)

def menu():
    while True:
        print("\n1.Create Manager\n2.Create Developer\n3.Check Inheritance\n4.Exit")
        ch = int(input("Choice: "))
        if ch == 1:
            m = Manager("Alice", 30, 101, 50000, "HR")
            m.display()
        elif ch == 2:
            d = Developer("Bob", 25, 102, 40000, "Python")
            d.display()
        elif ch == 3:
            print("Is Manager subclass of Employee?",
                  issubclass(Manager, Employee))
        elif ch == 4:
            break
        else:
            print("Invalid choice")

menu()