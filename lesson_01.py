username = input("Enter your username: ")

try:
    failed_attempts = int(input("Enter the number of failed logins: "))
except ValueError:
    print("Invalid input: please enter a whole number, such as 0, 2, or 5.")
else:
     print("checking login activity for:", username)
     print("Failed attempts:", failed_attempts)

     if failed_attempts < 0:
         print("Invalid input: failed attempts cannot be negative.")
     elif failed_attempts >= 3:
         print("Alert: repeated failed logins. Review this activity.")
     elif failed_attempts > 0:
         print("some failed logins recorded, below the alert threshold.")
     else:
         print("No failed logins recorded.")