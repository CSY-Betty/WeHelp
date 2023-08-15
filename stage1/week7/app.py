from flask import *
from url import app as myurl

app = Flask(__name__, static_folder="static", static_url_path="/")

app.secret_key = "This is Week 6."

app.register_blueprint(myurl)


app.run(port=3000)
