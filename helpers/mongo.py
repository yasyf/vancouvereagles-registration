from pymongo import MongoClient
import os

client = MongoClient(os.environ.get('MONGOLAB_URI'))
db = client[os.environ.get('MONGOLAB_URI').split('/')[-1]]
users = db.users
forms = db.forms
