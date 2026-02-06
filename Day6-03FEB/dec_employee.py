import csv

def employee_decorator(func):
    def wrapper(name):
        with open('employee_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'].lower() == name.lower():
                    return func(row)
        return "Employee not found"
    return wrapper


@employee_decorator
def get_employee_details(row):
    return f"Designation: {row['Designation']}, Salary: {row['Salary']}"


def get_all_employees():
    employees = []
    with open('employee_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row['Name'])
    return employees