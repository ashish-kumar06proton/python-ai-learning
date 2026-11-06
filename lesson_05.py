def check_login(failed_attempts):
    if failed_attempts >= 10:
        return "High alert: review this activity urgently."
    elif failed_attempts >= 3:
        return "Alert: review this login activity."
    elif failed_attempts > 0:
        return "Below the alert threshold."
    else:
        return "No failed logins recorded."


login_record = {
    "username": "Karan",
    "failed_attempts": 10
}

attempts = login_record["failed_attempts"]
result = check_login(attempts)

print("Username:", login_record["username"])
print("Failed attempts:", attempts)
print("Result:", result)