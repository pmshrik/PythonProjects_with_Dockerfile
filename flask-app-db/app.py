from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- Database setup ---
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL
           )"""
    )
    conn.commit()
    conn.close()

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["username"]
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return redirect(url_for("list_users"))

@app.route("/users")
def list_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return render_template("users.html", users=rows)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
