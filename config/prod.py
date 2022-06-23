from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())

USR = os.environ.get("DBUSR")
PWD = os.environ.get("DBPASS")
class prodConfig:
    MONGODB_URI = f"mongodb://{USR}:{PWD}@172.21.0.200:27017"