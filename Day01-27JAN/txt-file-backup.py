import shutil
import datetime

source="C:/Users/prava/OneDrive/Desktop/Capg training/Primary Track/data.txt"
backup=f"C:/Users/prava/OneDrive/Desktop/Capg training/Primary Track/data_backup_{datetime.date.today()}.txt"

shutil.copy(source, backup)
print(f"Backup of {source} created ay {backup}")