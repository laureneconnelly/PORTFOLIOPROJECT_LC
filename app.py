from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=postgres user=postgres password=admin123 host=localhost port=5432")

@app.route('/')
def index():
    return "<h>Hello, World!</h>"

@app.route("/song")
def song():
    cur = conn.cursor()
    cur.execute("SELECT * FROM songs")
    records = cur.fetchall()
    return render_template("musicfydesign.html", records=records)

@app.route("/artist")
def artist():
    cur = conn.cursor()
    cur.execute("SELECT * FROM artists")
    records = cur.fetchall()
    return render_template("musicfydesign.html", records=records)

@app.route("/album")
def album():
    cur = conn.cursor()
    cur.execute("SELECT * FROM albums")
    records = cur.fetchall()
    return render_template("musicfydesign.html", records=records)