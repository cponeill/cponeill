#! /usr/bin/env python2
from flask import Flask, render_template, jsonify, Response
from scraper import get_data

import os


app = Flask(__name__)


# The following functions all render to their corresponding HTML page and file.
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


@app.route("/projects/marketing")
def marketing():
    return render_template("marketing.html")


@app.route("/projects/development")
def development():
    return render_template("development.html")


@app.route("/api")
def api():
    return render_template("api.html")


@app.route("/api/data.json")
def api_return():
    return jsonify(get_data())


@app.route('/keybase.txt')
def keybase():
    return render_template("keybase.txt")
    

@app.after_request
def apply_caching(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'nonce-2726c7f38b'"
    response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'
    response.headers['X-Xss-Protection'] = '1'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response


# Running the server on port 5000.
if __name__ == "__main__ ":
    app.run()
