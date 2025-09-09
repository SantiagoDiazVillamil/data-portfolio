from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data-science")
def data_science():
    return render_template("data_science.html")

@app.route("/churn")
def churn():
    return render_template("churn.html")

@app.route("/anomalies")
def anomalies():
    return render_template("anomalies.html")

@app.route("/nlp")
def nlp():
    return render_template("nlp.html")

@app.route("/data-engineering")
def data_engineering():
    return render_template("data_engineering.html")

@app.route("/pipelines")
def pipelines():
    return render_template("pipelines.html")

@app.route("/streaming")
def streaming():
    return render_template("streaming.html")

@app.route("/automation")
def automation():
    return render_template("automation.html")
