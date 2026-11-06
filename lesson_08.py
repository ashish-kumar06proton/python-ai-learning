try:
    with open("login_report.txt", "r", encoding="utf-8") as report:
        contents = report.read()
except FileNotFoundError:
    print("Report not found. Run lesson_07.py to create it first.")
else:
    print(contents)
print(type(contents))