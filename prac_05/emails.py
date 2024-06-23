"""
Emails
Estimate: 45 minutes
"""



def extract_name_from_email(email):
    """Extract a name from the email address."""
    email_username = email.split('@')[0]
    parts = email_username.split('.')
    name = ' '.join(parts).title()
    return name


def main():
    emails_to_names = {}

    while True:
        email = input("Email: ").strip()

        if email == "":
            break

        name = extract_name_from_email(email)

        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirm not in ["", "y"]:
            name = input("Name: ").strip().title()

        emails_to_names[email] = name

    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


main()
