from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())

USR = os.environ.get("DBUSR")
PWD = os.environ.get("DBPASS")
class devConfig:
    MONGODB_URI = f"mongodb://{USR}:{PWD}@172.21.0.100:27017"
    