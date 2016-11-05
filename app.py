from flask import Flask, render_template, jsonify
import os
from scraper import get_data

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/focus")
def about():
	return render_template("focus.html")
	
@app.route("/skills")
def skills():
	return render_template("skills.html")

@app.route("/projects")
def projects():
	return render_template("projects.html")

@app.route("/api")
def api():
	return render_template("api.html")

@app.route("/api/data.json")
def api_return():
	return jsonify(get_data())

if __name__ == "__main__ ":
	app.run()