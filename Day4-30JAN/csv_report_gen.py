import csv
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "Los Angeles "},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}           
]
with open("report.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)    
print("CSV report generated successfully.")