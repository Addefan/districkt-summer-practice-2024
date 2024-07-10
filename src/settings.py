from os import getenv

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATABASE = {
    "USER": getenv("DB_USER", "mts-link-api"),
    "PASSWORD": getenv("DB_PASSWORD", "mts-link-api"),
    "HOST": getenv("DB_HOST", "localhost"),
    "PORT": getenv("DB_PORT", "5432"),
    "NAME": getenv("DB_NAME", "mts-link-api"),
}

DATABASE_URL = (f"postgresql+psycopg2://"
                f"{DATABASE['USER']}:{DATABASE['PASSWORD']}"
                f"@{DATABASE['HOST']}:{DATABASE['PORT']}/{DATABASE['NAME']}")

API_TOKEN = getenv("API_TOKEN")
