# __appsignal__.py
import os
from appsignal import Appsignal

# Load environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Get APPSIGNAL_PUSH_API_KEY from environment
push_api_key = os.getenv('APPSIGNAL_PUSH_API_KEY')
                         
appsignal = Appsignal(
    active=True,
    name="myblog",
    push_api_key=os.getenv("APPSIGNAL_PUSH_API_KEY"),
)