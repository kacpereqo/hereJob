import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from src.common.singleton import Singleton


class database(metaclass=Singleton):
    def __init__(self) -> None:
        uri, username, password = self.load_dotenv()
        connect_uri = uri.replace("<username>", username).replace("<password>", password)

        self.client:MongoClient = MongoClient(connect_uri, server_api=ServerApi('1'))

        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def load_dotenv(self) -> tuple[str,str,str]:
        """Loads .env file and returns MONGODB_URI, MONGODB_USERNAME, MONGODB_PASSWORD
        
        Return: tuple[str] - tuple containing in order uri, username and password
        """
        
        uri = os.environ.get("MONGODB_URI")
        username = os.environ.get("MONGODB_USERNAME")
        password = os.environ.get("MONGODB_PASSWORD")

        if uri is None or username is None or password is None:
            raise Exception("MONGODB credentials are invalid or missing!")

        return uri, username, password