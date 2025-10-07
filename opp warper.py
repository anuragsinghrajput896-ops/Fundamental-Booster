

class Employee:
    def __init__(self, employee_id=None, name=None, age=None, salary=None):
        self.__employee_id = employee_id   
        self.name = name
        self.age = age
        self.__salary = salary

    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, eid):
        self.__employee_id = eid

    def display(self):
        print(f"ID: {self.__employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.__salary}")

    def __del__(self):
      
        print(f"Employee object with ID {self.__employee_id} destroyed.")



class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")



class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")



def main():
    employees = []  

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Manager")
        print("2. Add Developer")
        print("3. Display All Employees")
        print("4. Check Inheritance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            eid = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            m = Manager(eid, name, age, salary, dept)
            employees.append(m)

        elif choice == "2":
            eid = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            d = Developer(eid, name, age, salary, lang)
            employees.append(d)

        elif choice == "3":
            print("\n--- Employee Details ---")
            for emp in employees:
                emp.display()
                print("----------------------")

        elif choice == "4":
            print("Is Manager subclass of Employee?", issubclass(Manager, Employee))
            print("Is Developer subclass of Employee?", issubclass(Developer, Employee))

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()