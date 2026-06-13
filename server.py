from flask import Flask, render_template, send_from_directory, session, redirect

from dotenv import load_dotenv

import sys

import os

load_dotenv(override=True)

# ------- INIT WEB SERVER ------ #

app = Flask(__name__)

# ------- INIT SESSIONS ------- #

app.secret_key = os.getenv("COOKIE_SECRET") or sys.exit("ERROR: Missing COOKIE_SECRET (secret code for sessions)")

# ------ ROUTES ------- #

@app.route("/")
def route_index():
    error = session.get("error")
    if error:
        session["error"] = None
    booking_success = session.get("booking_success", False)
    if booking_success:
        session["booking_success"] = False
    return render_template("index.html", error=error, booking_success=booking_success)

# ------- FAVICON -------- #

FAVICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "favicon")

def _send_favicon(filename: str, mimetype: str | None = None):
    resp = send_from_directory(FAVICON_DIR, filename, mimetype=mimetype)
    resp.headers["Cache-Control"] = "public, max-age=31536000, immutable"
    return resp

@app.route("/apple-touch-icon.png")
def apple_touch_icon():
    return _send_favicon("apple-touch-icon.png")

@app.route("/favicon-32x32.png")
def favicon_32():
    return _send_favicon("favicon-32x32.png")

@app.route("/favicon-16x16.png")
def favicon_16():
    return _send_favicon("favicon-16x16.png")

@app.route("/site.webmanifest")
def site_webmanifest():
    return _send_favicon("site.webmanifest", mimetype="application/manifest+json")

@app.route("/favicon.ico")
def favicon_ico():
    return _send_favicon("favicon.ico")

# ------ PAGE ROUTES ------ #

@app.route("/why")
def why():
    return render_template("why.html")

@app.route("/resource")
def resource():
    return render_template("resource.html")


# ------ LEGAL ROUTES ------ #

@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return redirect("/terms#privacy-policy", code=301)


@app.route("/refund")
def refund():
    return redirect("/terms#refund", code=301)

# --------- MAIN ----------- #

if __name__ == "__main__":
    app.run(debug=True, port=5023)