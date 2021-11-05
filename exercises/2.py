def is_valid_email(email):
    if "." in email and "@" in email:
        return True
    else:
        return False
email_input = input("Enter your email:\t")

if is_valid_email(email_input) == True:
    print(email_input + " is a valid email.")
else:
    print(email_input + " is an invalid email.")