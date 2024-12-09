import json
import os 

class Company:
    def __init__(self):
        self.workers = []

    def add_worker(self, worker):

        if any(w.name == worker.name for w in self.workers):
            print(f"Worker with the name {worker.name} already exists.")
        else:
            self.workers.append(worker)
            print(f"Worker {worker.name} added successfully.")

    def remove_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                print(f"Worker {worker_name} removed successfully.")
                return
        print(f"Worker with the name {worker_name} not found.")

    def list_workers(self):
        """
        Lists all workers in the company.
        """
        if not self.workers:
            print("No workers in the company.")
        else:
            print("Current workers:")
            for worker in self.workers:
                print(f"Name: {worker.name}, Age: {worker.age}, Salary: {worker.salary}, Role: {worker.role}")

    def find_worker(self, name):
        found = 0
        for worker in self.workers:
            if worker.name == name:
                found = 1
                return worker
        if found == 0:
            print("Worker not found.")
    
    def update_worker(self, worker):
        while True:
            print("What would you like to update?")
            print("1. Name")
            print("2. Age")
            print("3. Salary")
            print("4. Role")
            print("0. Exit")
            menu = int(input(">_"))
            if menu == 1:
                new_name = input("Input new worker name: ")
                worker.name = new_name
                print(f"{worker.name}'s name has been updated.")
            elif menu == 2:
                new_age = int(input("Input new worker age: "))
                worker.age = new_age
                print(f"{worker.name}'s age has been updated to {worker.age}")
            elif menu == 3:
                new_salary = float(input("Input new worker salary: "))
                worker.salary = new_salary
                print(f"{worker.name}'s salary has been updated to {worker.salary}")
            elif menu == 4:
                new_role = input("Input new worker role: ")
                worker.role = new_role
                print(f"{worker.name}'s role has been updated to {worker.role}")
            elif menu == 0:
                break
            else:
                print("Invalid input.")
    
    def sort_workers(self, by="name"):
        if by == "salary":
            self.workers.sort(key=lambda w: w.salary)
        elif by == "age":
            self.workers.sort(key=lambda w: w.age)
        elif by == "role":
            self.workers.sort(key=lambda w: w.role)
        else:
            self.workers.sort(key=lambda w: w.name)
        self.list_workers()

    def worker_retirement(self):
        for worker in self.workers:
            if worker.age >= 65:
                print(f"{worker.name} is able to retire. Age: {worker.age} years old.")
        cont = input("Continue?")
    
    def promote_worker(self, worker):
        while True: 
            print(f"Possible promotions for {worker.name}:")
            print(f"1. Senior {worker.role}")
            print(f"2. {worker.role} Manager")
            print(f"3. Executive {worker.role}")
            menu = int(input(">_"))
            if menu == 1:
                print(f"Worker {worker.name} has been promoted to Senior {worker.role}.")
                print(f"Worker salary has been increased from {worker.salary} to {worker.salary*1.2} (+20%)")
                worker.role = "Senior " + worker.role
                worker.salary *= 1.2
                break
            elif menu == 2:
                print(f"Worker {worker.name} has been promoted to {worker.role} Manager.")
                print(f"Worker salary has been increased from {worker.salary} to {worker.salary*1.5} (+50%)")
                worker.salary *= 1.5
                worker.role = worker.role + " Manager"
                break
            elif menu == 3:
                print(f"Worker {worker.name} has been promoted to Executive {worker.role}.")
                print(f"Worker salary has been increased from {worker.salary} to {worker.salary*2} (+100%)")
                worker.salary *= 2
                worker.role = "Executive " + worker.role
                break
            else:
                print("Invalid input.")



    def save_to_file(self, filename="company_data.json"):
        # Ensure file is saved in the same directory as this script
        file_path = os.path.join(os.path.dirname(__file__), filename)
        workers_data = [worker.__dict__ for worker in self.workers]
        with open(file_path, "w") as file:
            json.dump(workers_data, file, indent=4)
        print(f"Data saved to {file_path}.")



    def load_from_file(self, filename="company_data.json"):
        file_path = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(file_path, "r") as file:
                workers_data = json.load(file)
                self.workers = [Worker(**data) for data in workers_data]
            print(f"Data loaded from {file_path}.")
        except FileNotFoundError:
            print(f"No existing file found at {file_path}. Starting fresh.")
    

###


class Worker:
    def __init__(self, name, age, salary, role):
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
        
    def __str__(self):
        # Return a nicely formatted string for the Worker
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Role: {self.role}"
    


    ### CHATGPT MAGIC DON'T TOUCH ###

