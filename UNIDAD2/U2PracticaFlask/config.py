class BasicConfig:
    USER_DB = 'postgres'
    PASS_DB = 'admin'
    URL_DB = 'localhost'
    NAME_DB='Flask_db'
    FULL_URL= f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY="llave_secreta"
