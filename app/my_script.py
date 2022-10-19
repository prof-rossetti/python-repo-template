
import os
from dotenv import load_dotenv

load_dotenv() # will populate the environment with variables defined in the ".env" file

user_name = os.getenv("USER_NAME", default="Jon Snow")
password = os.getenv("PASSWORD")

print("HELLO," , user_name)

print("PASSWORD:", password)
