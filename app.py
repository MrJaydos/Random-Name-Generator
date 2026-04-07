from dotenv import load_dotenv
from src.NameParser.generate import clsGenerateNames

import os

load_dotenv()

api_key = os.getenv("API_KEY")


try:
    names = clsGenerateNames(api_key)
    if(names.generate(5)):
        for name in names._list:
            print(name) # Prints five random names. 
            details=names.details(name) # Returns all information on the name generated
except:
    print("An exception occurred")
