import csv

def profileGenerator(**kwargs):
    mylist = []
    for key, value in kwargs.items():
        mylist.append(f"{key} : {value}")
    return mylist

with open('employee_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        profile = profileGenerator(
            EmployeeID=row['EmployeeID'],
            Name=row['Name'].strip().title(),
            Department=row['Department'].strip().title(),
            Designation=row['Designation'].strip().title(),
            Salary=float(row['Salary']),
            Age=int(row['Age']),
            Gender=row['Gender'].strip().upper(),
            JoiningDate=row['JoiningDate'],
            Email=row['Email'].strip().lower()
        )
        print(profile)
        print("-" * 50)
