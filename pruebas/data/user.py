import os
from dotenv import load_dotenv

load_dotenv()
USER_VALID = {
    "email": os.getenv("STREMIO_EMAIL"),
    "password": os.getenv("STREMIO_PASSWORD")
}
