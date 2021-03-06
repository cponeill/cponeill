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
    """ This text file uses PGP as proof I am the admin of my own site. """
    return render_template("keybase.txt")
    
@app.route('/cyphernomicon.txt')
def cypher():
    """ Need to figure out how to pretty print this text file. """
    return render_template("cyphernomicon.txt")


@app.after_request
def apply_caching(response):
    """ Applying caching after request and also adding HTTP security headers. """
    #response.headers['Content-Security-Policy-Report-Only'] = "img-src self; script-src https://www.cponeill.com https://www.google-analytics.com/analytics.js"
    # Testing CSP headers in Report Only
    # response.headers['Content-Security-Policy-Report-Only'] = 'default-src self'
    response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'
    response.headers['X-Xss-Protection'] = '1'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response


# Running the server on port 5000.
if __name__ == "__main__ ":
    app.run()
