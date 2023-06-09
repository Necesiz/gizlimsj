import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
else:
    # Fill the Values
    API_ID = 15954332
    API_HASH = "85adea6f1eaf068b707703b4846a9ced"
    BOT_TOKEN = "6224251317:AAH27W1VgUhKUYIk5cgw6V1BEnNfGQUeDOc"
    DATABASE_URL = "mongodb+srv://hiyplva100:hiyplva100@cluster0.p1vcumr.mongodb.net/?retryWrites=true&w=majority"
