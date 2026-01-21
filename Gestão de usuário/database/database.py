import os
from playhouse.db_url import connect
from dotenv import load_dotenv

load_dotenv()

db = connect(os.getenv('DATABASE_URI'))