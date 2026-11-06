def check_login(failed_attempts):
    if failed_attempts >= 10:
        return "High alert: review this activity urgently."
    elif failed_attempts >= 3:
        return "Alert: review the login activity."
    elif failed_attempts > 0:
        return "Below the alert threshold."
    else:
        return "No failed logins recorded."


login_counts = [10,0,7,3,2]

for count in login_counts:
    Result = check_login(count)
    print(count, "->", Result)