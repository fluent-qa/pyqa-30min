# Lesson1: Setup your environment
from dotenv import load_dotenv
import os
import pickle

load_dotenv()
API_KEY = os.environ.get("API_KEY")
MY_APIKEY = os.environ.get("MY_APIKEY")
print(API_KEY)


def create_vectore_store():
    with open("vectorstore.pkl", "rb") as f:
        vectorstore = pickle.load(f)
    return vectorstore
