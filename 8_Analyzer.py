import numpy as np

print("==========Welcome to Numpy analyzer!==========")

class NumpyAnalyzer:

    def __init__(self):
        self.array = None

    def safeinput(self,message):
        while True:
            try:
                return int(input(message))
            except Exception:
                print("Invalid input! Please enter valid input!!")

    def create(self):
        while True:
            print("\nSelect the type of array to create:")
            print("Enter 1 for create 1D array")
            print("Enter 2 for create 2D array")
            print("Enter 0 for go to the main menu!\n")

            crchoice = self.safeinput("Enter your choice: ")

            try:
                if crchoice == 1:
                    num = list(map(int, input("Enter elements (space separated): ").split()))
                    self.array = np.array(num)
                
                elif crchoice == 2:
                    row = self.safeinput("Enter number of rows: ")
                    column = self.safeinput("Enter number of columns: ")
                    num = list(map(int, input(f"Enter {row*column} elements: ").split()))

                    if len(num) != row*column:
                        print("Incorrect number of elements!")
                        continue

                    self.array = np.array(num).reshape(row, column)
                
                elif crchoice == 0:
                    break

                else:
                    print("Invalid choice!!")

                print("\nArray created successfully!")
                print(self.array)

                while True:

                    print("\nChoose an operation:")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. More Operations")
                    print("0. Back to Create Menu")

                    op = self.safeinput("Enter your choice: ")

                    if op == 1:
                        if self.array.ndim == 2:
                            r = self.safeinput("Enter row index: ")
                            c = self.safeinput("Enter column index: ")
                            print("Element:", self.array[r][c])
                        else:
                            i = self.safeinput("Enter index: ")
                            print("Element:", self.array[i])

                    elif op == 2:
                        if self.array.ndim == 2:
                            r = input("Enter the row range (start:end): ")
                            c = input("Enter the column range (start:end): ")

                            rs, re = map(int, r.split(":"))
                            cs, ce = map(int, c.split(":"))

                            sliced = self.array[rs:re, cs:ce]

                            print("\nSliced Array:")
                            print(sliced)
                        else:
                            r = input("Enter range (start:end): ")
                            rs, re = map(int, r.split(":"))
                            print("Sliced Array:", self.array[rs:re])

                    elif op == 3:

                        while True:
                            print("\nMore Operations:")
                            print("1. Show Shape")
                            print("2. Show Size")
                            print("3. Show Dimensions")
                            print("0. Back")

                            sub = self.safeinput("Enter your choice: ")

                            if sub == 1:
                                print("Shape:", self.array.shape)

                            elif sub == 2:
                                print("Size:", self.array.size)

                            elif sub == 3:
                                print("Dimensions:", self.array.ndim)

                            elif sub == 0:
                                break

                            else:
                                print("Invalid choice!")

                    elif op == 0:
                        break

                    else:
                        print("Invalid choice!")
            
            except Exception:
                    print("Invalid input! Please enter only integers!")

    def math(self):

        while True:

            if self.array is None:
                print("Create an array first!")
                return
            
            print("\nChoose a Mathematical operation:")
            print("Enter 1 for Addition")
            print("Enter 2 for Subtraction")
            print("Enter 3 for Multiplication")
            print("Enter 4 for Division")
            print("Enter 5 for Dot Product (1D only)!")
            print("Enter 6 for Matrix Multiplication (2D only)!")
            print("Enter 0 for go to the main menu!\n")

            mchoice = self.safeinput("Enter your choice: ")

            if mchoice==0:
                break
            
            try:
                elements = list(map(int, input(f"Enter {self.array.size} elements for second array (same as first array): ").split()))
                second_array = np.array(elements).reshape(self.array.shape)

                if mchoice == 1:
                    print("Result:\n", self.array + second_array)

                elif mchoice==2:
                    print("Result: \n", self.array-second_array)

                elif mchoice==3:
                    print("Result: \n", self.array*second_array)

                elif mchoice==4:
                    print("Result: \n", self.array/second_array)
                
                elif mchoice == 5:
                    if self.array.ndim == 1:
                        print("Dot Product:", np.dot(self.array, second_array))
                    else:
                        print("Dot product only for 1D arrays!")

                elif mchoice == 6:
                    if self.array.ndim == 2:
                        print("Matrix Multiplication:\n", np.matmul(self.array, second_array))
                    else:
                        print("Matrix multiplication only for 2D arrays!")
                else:
                    print("Invalid choice!!")

            except ValueError:
                print("Invalid input or reshape error!")
            except ZeroDivisionError:
                print("Division by zero not allowed!")

    def combine_split(self):

        while True:
            if self.array is None:
                print("Create an array first! ")
                return
            
            print("\nChoose an option: ")
            print("Enter 1 for Combine (Vertical Stack)")
            print("Enter 2 for Combine (Horizontal Stack)")
            print("Enter 3 for Split Array")
            print("Enter 0 for go to the main menu!\n")

            schoice = self.safeinput("Enter your choice: ")

            try:
                if schoice == 1:
                    elements = list(map(int, input(f"Enter {self.array.size} elements for second array (same as first array):").split()))
                    second_array = np.array(elements).reshape(self.array.shape)

                    combined = np.vstack((self.array, second_array))
                    print("Vertically Combined Array:\n", combined)

                elif schoice == 2:
                    elements = list(map(int, input(f"Enter {self.array.size} elements for second array (same as first array): ").split()))
                    second_array = np.array(elements).reshape(self.array.shape)

                    combined = np.hstack((self.array, second_array))
                    print("Horizontally Combined Array:\n", combined)

                elif schoice==3:
                    parts = self.safeinput("Enter number of splits: ")
                    if self.array.ndim == 2:
                        split_arrays = np.vsplit(self.array, parts)
                    else:
                        split_arrays = np.array_split(self.array, parts)
                    
                    for arr in split_arrays:
                        print(arr)
                
                elif schoice==0:
                    break
                
                else:
                    print("Invalid choice!")
                
            except Exception:
                print("Error while combining or splitting!")

    def filter(self):
            
        while True:
            if self.array is None:
                print("Create an array first!")
                return
            
            print("\nChoose an option: ")
            print("Enter 1 for Search values!")
            print("Enter 2 for Sort the values!")
            print("Enter 3 for Filter values!")
            print("Enter 0 for go to the main menu!\n")

            fchoice = self.safeinput("Enter your choice: ")

            if fchoice==1:
                value = self.safeinput("Enter value to search: ")
                result = np.where(self.array == value)
                
                if result[0].size == 0:
                    print("Value not found!")
                else:
                    print("Value found at index:", result)

            elif fchoice==2:
                print("Sorted Array:\n", np.sort(self.array))
                
            elif fchoice==3:
                value = self.safeinput("Enter value: ")
                print("Filtered Values:\n", self.array[self.array > value])

            elif fchoice==0:
                break
            
            else:
                print("Invalid choice!")

    def statistics(self):

        while True:
            if self.array is None:
                print("Create an array first!")
                return
            
            print("\nChoose an aggregate/statistical operation:")
            print("Enter 1 for Sum")
            print("Enter 2 for Mean")
            print("Enter 3 for Median")
            print("Enter 4 for Standard Deviation")
            print("Enter 5 for Variance")
            print("Enter 6 for Min & Max")
            print("Enter 0 for go to the main menu!\n")
            
            stchoice = self.safeinput("Enter your choice: ")

            if stchoice==1:
                print("Sum:", np.sum(self.array))

            elif stchoice==2:
                print("Mean:", np.mean(self.array))

            elif stchoice==3:
                print("Median:", np.median(self.array))

            elif stchoice==4:
                print("Standard Deviation:", np.std(self.array))

            elif stchoice==5:
                print("Variance:", np.var(self.array))

            elif stchoice==6:
                print("Min:", np.min(self.array))
                print("Max:", np.max(self.array))

            elif stchoice==0:
                break

            else:
                print("Invalid choice!")

def main():
    obj = NumpyAnalyzer()

    while True:
        print("\nChoose an option:")
        print("Enter 1 for Create array!")
        print("Enter 2 for Mathematical operation!")
        print("Enter 3 for Combine or Split Arrays!")
        print("Enter 4 for Search, Sort, Filter!")
        print("Enter 5 for Aggregates and Statistics!")
        print("Enter 0 for exit!\n")

        choice = obj.safeinput("Enter your choice: ")

        if choice == 1:
            obj.create()

        elif choice == 2:
            obj.math()

        elif choice == 3:
            obj.combine_split()

        elif choice == 4:
            obj.filter()

        elif choice == 5:
            obj.statistics()

        elif choice == 0:
            print("Thank you for using Numpy analyzer! Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()