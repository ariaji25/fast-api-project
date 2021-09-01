from dotenv import dotenv_values


class Config:
    config = dotenv_values(".env") 
    DB_URL = config['DB_URL']
    DB_URL_TEST = "sqlite:///db_test.db"