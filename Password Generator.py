import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Specify the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()