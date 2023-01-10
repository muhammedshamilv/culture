import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
dbname = os.getenv('DATABASE_NAME')

