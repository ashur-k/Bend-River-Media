import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/wedding_services")
def wedding_services():
    return render_template("wedding_services.html")

@app.route("/videography-services")
def videography_services():
    return render_template("videography_services.html")

@app.route("/photography_services")
def photography_services():
    return render_template("photography_services.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")

@app.route("/BRM_portfolio")
def BRM_portfolio():
    return render_template("BRM_portfolio.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(5000),
            debug=True)