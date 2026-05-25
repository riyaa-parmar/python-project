
print("Welcome to my pattern generator and number analyzer!")
while True:
    print()

    print("select option: ")
    print("1. Generate pattern")
    print("2. Analyze range of number")
    print("3. Exit")

    print()

    choice = int(input("enter your choice: "))
    if choice == 1:
        pattern = int(input("enter the numbers of row for pattern: "))
        print("pattern: ")
        for i in range(1,pattern+1):
            for j in range(i):
                print("*",end=" ")
            print()

    elif choice == 2:
        start = int(input("enter the start of range: "))
        end = int(input("enter the end of range: "))
        total=0
        for i in range(start,end+1):
            total += i
            if i %2==0:
                print("number",i,"is even")
            else:
                print("number",i,"is odd")
        print("the sum of all num is: ", total)
    else:
        break

print()

print("thanks for your attention!")
