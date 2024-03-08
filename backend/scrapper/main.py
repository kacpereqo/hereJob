from dotenv import load_dotenv
from src.service import ScrapperService

if __name__ == "__main__":
    load_dotenv()

    service = ScrapperService()
    service.start()

