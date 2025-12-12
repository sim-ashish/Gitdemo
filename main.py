from login import UserAuthentication
from utils import hash_password
auth = UserAuthentication()


print("-----------------WELCOME TO THE LOAN DEPARTMENT-------------------")
print("Please login to continue")
username = input("Enter your username: ")
password = input("Enter your password: ")
hashed_password = hash_password(password)

if not auth.healthcheck():
    print("Server is down. Please try again later.")

if auth.login(username, hashed_password):
    print("Login successful!")
else:
    print("Invalid username or password.")