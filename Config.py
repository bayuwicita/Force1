import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

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
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 24515526
    API_HASH = "482182f8ab9dd82fb9144a0f68eeb817"
    BOT_TOKEN = "5871159415:AAEmdLPpLY_8maR5xPCMCR3GIVg9-tFBqVs"
    DATABASE_URL = "postgres://wlsokvlw:iXaEM2r2BjhK5GcOXGm2qJWotsCjChR0@floppy.db.elephantsql.com/wlsokvlw"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "nekopoisupport"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
        
DEVS = [1744109441, 1946995626]
