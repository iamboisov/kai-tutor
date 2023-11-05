import os
from dotenv import load_dotenv

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')
OPENAI_KEY = os.getenv('OPENAI_KEY')
ADMIN_ID = os.getenv('ADMIN_ID')
ELEVEN_LABS = os.getenv('ELEVEN_LABS')

