def check_login(failed_attempts):
    if failed_attempts >=10:
        return "High Alert: review this activity urgently."
    elif failed_attempts >= 3:
        return "Alert: review this login activity."
    elif failed_attempts > 0:
        return "Below the alert threshold."
    else:
        return "No failed logins recorded."


while True:
    try:
        attempts = int(input("Enter the number of failed logins: "))
    except ValueError:
        print("Please enter a whole number")
        continue

    if attempts < 0:
        print("The number cannot be negative.")
        continue
    
    break


result = check_login(attempts)
print(result)