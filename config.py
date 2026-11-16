import os
from secrets import token_hex

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or token_hex(32)

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
