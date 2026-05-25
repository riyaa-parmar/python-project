import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("========== Data Analysis and Visualization Program ==========")

class Data:

    def __init__(self):
        self.data = None

    def safeinput(self,message):
        while True:
            try:
                return int(input(message))
            except Exception:
                print("Invalid input! Please enter valid input!!")

    def DataLoad(self,file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except FileNotFoundError:
            print("File not found! Please check path!") 
        except Exception as e:
            print("Error loading dataset:",e)

    def DataExplore(self):
        while True:

            try:
                if self.data is None:
                    print("Dataset not loaded!")
                    return

                print("\n=== Explore Data ===")
                print("1. Display the First 5 Rows.")
                print("2. Display the Last 5 Rows.")
                print("3. Display Column Name.")
                print("4. Display Datatype.")
                print("5. Display Basic Info.")
                print("0. Go to Main Menu.\n")

                echoice = self.safeinput("Enter your choice: ")

                if echoice == 1:
                    print(self.data.head())

                elif echoice == 2:
                    print(self.data.tail())

                elif echoice == 3:
                    print(self.data.columns)

                elif echoice == 4:
                    print(self.data.dtypes)

                elif echoice == 5:
                    self.data.info()

                elif echoice == 0:
                    break

                else:
                    print("Invalid choice!!")
    
            except Exception as e:
                print("Error exploring data:", e)

    def DataFrame_Operation(self):
        
        while True:
            try:
                if self.data is None:
                    print("Dataset not loaded!")
                    return
                
                print("\n=== DataFrame Operation ===")
                print("1. Mathematical Operation (sum, mean, max, min)")
                print("2. Search Data.")
                print("3. Sort Data.")
                print("4. Filter Data.")
                print("5. Aggregation Function.")
                print("6. Create Pivot Table.")
                print("0. Go to Main Menu.\n")

                dfchoice = self.safeinput("Enter Your choice: ")
                
                if dfchoice == 1:
                    print("\nSum: ", self.data.sum(numeric_only=True))
                    print("\nMean: ", self.data.mean(numeric_only=True))
                    print("\nMax: ", self.data.max(numeric_only=True))
                    print("\nMin: ", self.data.min(numeric_only=True))

                elif dfchoice == 2:
                    column = input("Enter Column name to search: ")
                    if column not in self.data.columns:
                        print("Column not found!")
                    else:
                        value = input("Enter Value to search: ")
                        print(self.data[self.data[column] == value])
                
                elif dfchoice == 3:
                    column = input("Enter Column name to Sort: ")
                    if column not in self.data.columns:
                        print("Column not found!")
                    else:
                        print(self.data.sort_values(by=column))

                elif dfchoice == 4:
                    column = input("Enter Column Name to Filter: ")
                    if column not in self.data.columns:
                        print("Column not found!")
                    else:
                        value = input("Enter Value: ")
                        print(self.data[self.data[column] == value])

                elif dfchoice == 5:
                    column = input("Enter column name for aggregation: ")
                    if column not in self.data.columns:
                        print("Column not found!")
                    else:
                        print(self.data.groupby(column).sum(numeric_only=True))
                    
                elif dfchoice == 6:
                    index = input("Enter index column: ")
                    columns = input("Enter column for pivot: ")
                    values = input("Enter value column: ")

                    pivot = pd.pivot_table(
                        self.data,
                        values=values,
                        index=index,
                        columns=columns,
                        aggfunc="sum"
                    )

                    print(pivot)

                elif dfchoice == 0:
                    break

                else:
                    print("Invalid choice!")

            except Exception as e:
                print("Error in DataFrame operations:", e)

    def Missing_Data(self):
        while True:
            try:
                if self.data is None:
                    print("Dataset not loaded!")
                    return
                
                print("\n=== Handle Missing Data ===")
                print("1. Display row with Missing values.")
                print("2. Fill Missing value with Mean.")
                print("3. Drop row with Missing values")
                print("4. Replace Missing value with specific value")
                print("0. Go to Main Menu.\n")

                mchoice = self.safeinput("Enter your choice: ")

                if mchoice == 1:
                    print(self.data[self.data.isnull().any(axis=1)])

                elif mchoice == 2:
                    self.data.fillna(self.data.mean(numeric_only=True),inplace=True)
                    print("Missing value filled with Mean!")

                elif mchoice == 3:
                    self.data.dropna(inplace=True)
                    print("Rows with missing values dropped!")

                elif mchoice == 4:
                    value = input("Enter replacement value: ")
                    self.data.fillna(value, inplace=True)
                    print("Missing values replaced.")

                elif mchoice == 0:
                    break

                else:
                    print("Invalid choice!")

            except ValueError:
                print("Please Enter a Valid Number!")
            except Exception as e:
                print("Error handling missing data:",e)

    def Statistic(self):
        try:
            if self.data is None:
                print("Dataset not loaded!")
                return

            print("\nStatistical Summary:")
            print(self.data.describe())

            print("\nStandard Deviation:")
            print(self.data.std(numeric_only=True))

            print("\nVariance:")
            print(self.data.var(numeric_only=True))

        except Exception as e:
            print("Error in statistical analysis:", e)

    def Data_Visualization(self):

        while True:
            try:
                if self.data is None:
                    print("Dataset not Loaded!")
                    return
                
                print("\n=== Data Visualization ===")
                print("1. Bar Plot")
                print("2. Line Plot")
                print("3. Scatter Plot")
                print("4. Pie Chart")
                print("5. Histogram")
                print("6. Seaborn Heatmap")
                print("7. Stack Plot")
                print("0. Go to Main Menu.\n")
                
                dachoice = self.safeinput("Enter your choice: ")

                if dachoice == 1:
                    self.data.groupby("Product")["Sales"].sum().plot(kind="bar")
                    plt.title("Sales by Product")

                elif dachoice == 2:
                    self.data.plot(x="Year",y="Sales",kind="line")
                    plt.title("Sales Trend")

                elif dachoice == 3:
                    x = input("Enter x column: ")
                    y = input("Enter y column: ")
                    plt.scatter(self.data[x],self.data[y])
                    plt.xlabel(x)
                    plt.ylabel(y)

                elif dachoice == 4:
                    self.data.groupby("Region")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
                    plt.title("Sales by Region")

                elif dachoice == 5:
                    self.data["Sales"].plot(kind="hist", bins=10)
                    plt.title("Sales Distribution")

                elif dachoice == 6:
                    corr = self.data.corr(numeric_only=True)
                    sns.heatmap(corr, annot=True)

                elif dachoice == 7:
                    x = self.data["Year"]
                    y1 = self.data["Sales"]
                    plt.stackplot(x, y1)
                    plt.title("Stack Plot Example")

                elif dachoice == 0:
                    break

                else:
                    print("Invalid choice!")

                plt.show()

            except Exception as e:
                print("Error generating visualization:", e)

    def save_visualization(self):
        try:
            name = input("Enter file name (example: plot.png): ")
            plt.savefig(name)
            print("Visualization saved successfully!")

        except Exception as e:
            print("Error saving visualization:", e)


def Main_Menu():

    obj = Data()

    while True:
        try:
            print("\n1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("0. Exit\n")

            choice = obj.safeinput("Enter your choice: ")

            if choice == 1:
                path = input("Enter CSV file path: ")
                obj.DataLoad(path)

            elif choice == 2:
                obj.DataExplore()

            elif choice == 3:
                obj.DataFrame_Operation()

            elif choice == 4:
                obj.Missing_Data()

            elif choice == 5:
                obj.Statistic()

            elif choice == 6:
                obj.Data_Visualization()

            elif choice == 7:
                obj.save_visualization()

            elif choice == 0:
                print("Exiting the program. Thank you! Goodbye!")
                break

            else:
                print("Invalid choice!")
                
        except Exception as e:
            print("Error:", e)

Main_Menu()