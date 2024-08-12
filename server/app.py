import os
import random
import string

from flask import Flask

from models import init_app as db_init_app, db
from resources import api


app = Flask(__name__, static_folder="static", static_url_path="/")

# configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 300  # Таймаут в секундах
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

# init api
api.init_app(app)

# init db
with app.app_context():
    db_init_app(app)

# make env
MEGA_SECRET_KEY = ''.join(
    random.choices([*string.ascii_letters, *string.digits], k=100)
)
os.environ.update({
    "DATABASE_URI": os.getenv("DATABASE_URI"), 
    "AUTH_KEY": MEGA_SECRET_KEY
})
print("secret app key:", MEGA_SECRET_KEY)


if __name__ == "__main__":
    app.run(port=8080)
