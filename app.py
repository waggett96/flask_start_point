from os import environ
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lots and lots of random strings'

# -----------------------------------------------------------------------------
# HOME
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html.j2")

# MUSIC
@app.route("/music")
def music():
    return render_template("music.html.j2")

# STORY
@app.route("/story")
def story():
    return render_template("story.html.j2")

# MERCH
@app.route("/merch")
def merch():
    return render_template("merch.html.j2")

# -----------------------------------------------------------------------------
# ERROR HANDLING PAGES
@app.errorhandler(400)
def not_found(e):
    return render_template("error_pages/400.html")
@app.errorhandler(404)
def not_found(e):
    return render_template("error_pages/404.html")
@app.errorhandler(408)
def not_found(e):
    return render_template("error_pages/408.html")
@app.errorhandler(500)
def not_found(e):
    return render_template("error_pages/500.html")
@app.errorhandler(502)
def not_found(e):
    return render_template("error_pages/502.html")

# -----------------------------------------------------------------------------
################################## RUN APP ##################################
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
