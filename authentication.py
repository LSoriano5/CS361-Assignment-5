import os

USERS_FILE = "users.txt"

def user_exists(username):
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            users = file.readlines()
            for user in users:
                if user.split(":")[0] == username:
                    return True
    return False

def register_user(username, password):
    if user_exists(username):
        print(f"Username {username} already exists.")
    else:
        with open(USERS_FILE, "a") as file:
            file.write(f"{username}:{password}\n")
        print(f"User {username} registered successfully!")
        print("\nWelcome to Music App!")

def login_user(username, password):
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            users = file.readlines()
            for user in users:
                stored_username, stored_password = user.strip().split(":")
                if stored_username == username and stored_password == password:
                    print(f"Welcome back, {username}!")
                    return True
    print("Invalid credentials, please try again.")
    return False

def logout_user():
    print("Logging out...")

