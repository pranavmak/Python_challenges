import datetime
import os

current_datetime = datetime.datetime.now()
print(f"Current date and time is: {current_datetime}")

try:
    user_name = os.getlogin()
    print(f"Current logged in user is: {user_name}")
except OSError:
    print("User login information not available in this environment")
