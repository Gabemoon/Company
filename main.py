from classes import Company, Worker
# Create a company instance
my_company = Company()
my_company.load_from_file()

while True:
    print("Select an option: ")
    print("1. Add Worker(s)")
    print("2. Remove Worker")
    print("3. List Workers")
    print("4. Search Worker")
    print("5. Update Worker")
    print("6. Sort Workers")
    print("7. Worker Retirement")
    print("8. Promote Worker")
    print("0. Exit")
    menu = int(input(">_ "))
    if menu == 0:
        my_company.save_to_file()
        break
    elif menu == 1:
        n = int(input("How many workers would you like to add? "))
        for i in range(n):
            print(f"\nEntering details for worker {i + 1}:")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            role = input("Enter role: ")

            worker = Worker(name, age, salary, role)
            my_company.add_worker(worker)
    elif menu == 2:
        worker = input("What is the name of the worker you wish to remove? ")
        my_company.remove_worker(worker)
    elif menu == 3:
        my_company.list_workers()
    elif menu == 4:
        worker = input("What is the name of the worker you'd want to find? ")
        print(my_company.find_worker(worker))
    elif menu == 5:
        worker = input("What is the name of the worker you'd want to change parameters? ")
        worker_to_update = my_company.find_worker(worker)
        my_company.update_worker(worker_to_update)
    elif menu == 6:
        print("Sort Workers by: ")
        print("1. Name")
        print("2. Age")
        print("3. Role")
        print("4. Salary")
        menu2 = int(input(">_"))
        if menu2 == 1:
            my_company.sort_workers(by="name")
        elif menu2 == 2:
            my_company.sort_workers(by="age")
        elif menu2 == 3:
            my_company.sort_workers(by="role")
        elif menu2 == 4:
            my_company.sort_workers(by="salary")
        else:
            print("Invalid input.")
    elif menu == 7:
        my_company.worker_retirement()
    elif menu == 8:
        worker = input("Enter the name of the worker: ")
        my_company.promote_worker(my_company.find_worker(worker))
    else:
        print("Invalid input.")