from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv('.dbenv'))

USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DB_NAME = os.environ.get('DB_NAME')