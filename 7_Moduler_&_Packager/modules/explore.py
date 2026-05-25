def explore_menu():
    module_name = input("Enter module name (math/random/datetime): ")

    try:
        module = __import__(module_name)
        print(dir(module))
    except Exception:
        print("Module not found")