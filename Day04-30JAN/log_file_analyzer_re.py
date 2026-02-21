import re

log_file = "application.log"

pattern = re.compile(
    r"(\d{4}-\d{2}-\d{2})\s+"
    r"(\d{2}:\d{2}:\d{2})\s+"
    r"(INFO|ERROR|WARN)\s+"
    r"\[(.*?)\]\s+"
    r"(.*)"
)

with open(log_file, "r") as file:
    for line in file:
        match = pattern.match(line)
        if match:
            date, time, level, module, message = match.groups()

            print(f"Date    : {date}")
            print(f"Time    : {time}")
            print(f"Level   : {level}")
            print(f"Module  : {module}")
            print(f"Message : {message}")
            print("-" * 40)