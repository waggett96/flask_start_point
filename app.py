from os import environ
from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'

# -----------------------------------------------------------------------------
# HOME
@app.route("/")
def home():
    return render_template("base.html")

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

# -----------------------------------------------------------------------------
################################## RUN APP ##################################
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
