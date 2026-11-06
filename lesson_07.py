def check_login(failed_attempts):
    if failed_attempts >=10:
        return "High alert: review this activity urgently."
    elif failed_attempts >= 3:
        return "Alert: review this login activity."
    elif failed_attempts > 0:
        return "Below the alert threshold."
    else:
        return "No failed login recorded."


login_records = [
    {"username": "Ashish", "failed_attempts": 0},
    {"username": "Karan", "failed_attempts": 4},
    {"username": "Sara", "failed_attempts": 12},
    {"username": "Mika", "failed_attempts": 3},
    {"username": "Leena", "failed_attempts": 10}
]

alert_users = []

for record in login_records:
    username = record["username"]
    attempts = record["failed_attempts"]
    result = check_login(attempts)

    print(username, "->", attempts, "->", result)

    if attempts >= 3:
    
        alert_users.append(username)


print("Total records triggering alerts:", len(alert_users))
print("Users to review:", alert_users)
print("Total records checked:", len(login_records))

with open("login_report.txt", "w", encoding="utf-8") as report:
    report.write("Login Activity Report\n")
    report.write("Total records checked: " + str(len(login_records)) + "\n")
    report.write("Records triggering alerts: " + str(len(alert_users)) + "\n")

    for username in alert_users:
        report.write(username +"\n")

print("Report saved to login_report.txt")
