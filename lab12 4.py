
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = [employee1, employee2, employee3]


for employee in employees:
    name, id, department, salary = employee
    print(f"Name: {name}")
    print(f"ID: {id}")
    print(f"Department: {department}")
    print(f"Salary: {salary}")
    print() 
