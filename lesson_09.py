import json


def check_login(failed_attempts):
    if failed_attempts >= 10:
        return "High alert: review this activity urgently."
    elif failed_attempts >= 3:
        return "Alert: review this login activity."
    elif failed_attempts > 0:
        return "Below the alert threshold."
    else:
        return "No failed logins recorded."


with open("login_records.json", "r", encoding="utf-8") as file:
    login_records = json.load(file)

alert_users = []

for record in login_records:
    username = record["username"]
    attempts = record["failed_attempts"]
    result = check_login(attempts)

    print(username, "->", attempts, "->", result)

    if attempts >= 3:
        alert_users.append(username)

print("Total records checked:", len(login_records))
print("Records triggering alerts:", len(alert_users))
print("Users to review:", alert_users)