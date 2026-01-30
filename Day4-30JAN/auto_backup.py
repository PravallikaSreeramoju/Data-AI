import shutil
import datetime

source=r"C:\Users\prava\OneDrive\Desktop\python\day-4\tasks.txt"
back_up=fr"C:\Users\prava\OneDrive\Desktop\python\day-4\backup_tasks_{datetime.date.today()}.txt"

shutil.copy(source,back_up)
print("Backup created successfully")