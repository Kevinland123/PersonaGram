"""ala development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\x05\x1fii\xe2w\xa9$$\xad\x16s\xd6\x08\xdc\x93\x9e\x03\x88g\xcc{\x9e\xb0'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
ALA_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = ALA_ROOT/'var'/'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/ala.sqlite3
DATABASE_FILENAME = ALA_ROOT/'var'/'ala.sqlite3'

POSTGRESQL_DATABASE_HOST = "ala-personagram.ctj3mfrzha94.us-east-2.rds.amazonaws.com"
POSTGRESQL_DATABASE_PORT = 5432
POSTGRESQL_DATABASE_USER = "personagram"
POSTGRESQL_DATABASE_PASSWORD = "biZljqpi5XXgeb1YCZZP"
POSTGRESQL_DATABASE_DB = "personagram"