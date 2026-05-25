dataset = []
summary = {}

def input_data():
    global dataset
    choice = int(input("1. 1D List\n2. 2D List\nChoose: "))
    if choice == 1:
        dataset = list(map(int, input("Enter values: ").split()))
    else:
        rows = int(input("Rows: "))
        dataset = []
        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            dataset.append(row)
    print("Data stored successfully.")

def data_summary():
    flat = flatten(dataset)
    print("Total elements:", len(flat))
    print("Min:", min(flat))
    print("Max:", max(flat))
    print("Sum:", sum(flat))

def flatten(data):
    if all(isinstance(i, list) for i in data):
        return [x for row in data for x in row]
    return data

def average(*args):
    return sum(args) / len(args)

def stats(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def filter_data():
    t = int(input("Enter threshold: "))
    flat = flatten(dataset)
    result = list(filter(lambda x: x > t, flat))
    print("Filtered data:", result)

def sort_data():
    flat = flatten(dataset)
    print("Original:", flat)
    print("sorted():", sorted(flat))
    flat.sort()
    print("sort():", flat)

def dataset_statistics():
    global summary
    flat = flatten(dataset)
    summary = {
        "Min": min(flat),
        "Max": max(flat),
        "Sum": sum(flat),
        "Average": average(*flat)
    }
    stats(**summary)

def menu():
    while True:
        print("\n1.Input Data\n2.Summary\n3.Factorial\n4.Filter\n5.Sort\n6.Stats\n7.Exit")
        ch = int(input("Choice: "))
        if ch == 1:
            input_data()
        elif ch == 2:
            data_summary()
        elif ch == 3:
            n = int(input("Number: "))
            print("Factorial:", factorial(n))
        elif ch == 4:
            filter_data()
        elif ch == 5:
            sort_data()
        elif ch == 6:
            dataset_statistics()
        elif ch == 7:
            print("Exit")
            break
        else:
            print("Invalid choice")

menu()