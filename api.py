# api.py
from dotenv import load_dotenv
load_dotenv()
import flask
from mongo import load_db


app = flask.Flask(__name__)
app.config["DEBUG"] = True

db = load_db()

@app.route("/", methods=["GET"])
def home():
    return "<h1>Payoff API</h1><p>Back-end to the Payoff Budget Application</p>"


app.run()
