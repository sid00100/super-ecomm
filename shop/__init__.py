from flask import Flask

import firebase_admin

from firebase_admin import credentials


app = Flask(__name__)

cred = credentials.Certificate(
    "shop/super-ecomm-firebase-adminsdk-ra9ne-c10790be00.json")

firebase_admin.initialize_app(cred)
