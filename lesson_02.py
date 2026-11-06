username = input("Enter your username: ")

while True:
    try:
        failed_attempts = int(input("Enter the number of failed logins: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if failed_attempts < 0:
        print("The number cannot be nagative.")
        continue

    print("Input accepted.")

    break

print("Checking login activity for:", username)
print("Failed attempts:", failed_attempts)

if failed_attempts >= 3:
    print("Alert: repeated failed logins. Review this activity.")
elif failed_attempts > 0:
    print("Some failed logins recorded, below the alert threshold.")
else:
    print("No failed logins recorded.")

            