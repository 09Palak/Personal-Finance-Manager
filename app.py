from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="finance_manager"
)

cursor = db.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    return render_template("index.html", expenses=data)

@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form["title"]
    amount = request.form["amount"]
    category = request.form["category"]

    query = "INSERT INTO expenses (title, amount, category) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, amount, category))
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
