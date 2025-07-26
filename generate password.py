import random
import string
def generate_password(len):
    if len < 5:
        print("Password length should be at least 5 characters for good security.")
        return ""
    charac = string.ascii_letters + string.digits + string.punctuation
    paswrd = ''.join(random.choice(charac) for i in range(len))
    return paswrd
def main():
    try:
        len = int(input("Enter the desired length of the password: "))
        paswrd = generate_password(len)
        if paswrd:
            print(f"\nGenerated Password: {paswrd}")
    except ValueError:
        print("Please enter a valid number.")
main()
