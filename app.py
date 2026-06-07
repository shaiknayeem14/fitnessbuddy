from flask import Flask, render_template, request, redirect
from flask import session
from flask import flash
import sqlite3

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from config import Config
from models.user import create_tables

app = Flask(__name__)
app.config.from_object(Config)

create_tables()


def get_db():

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    return conn


@app.route("/")
def home():

    if "user_id" not in session:
        return redirect("/login")

    conn = get_db()

    user = conn.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    conn.close()

    return render_template(
        "dashboard.html",
        user=user
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        age = request.form["age"]
        height = request.form["height"]
        weight = request.form["weight"]
        goal = request.form["goal"]

        hashed = generate_password_hash(password)

        conn = get_db()

        try:

            conn.execute("""
            INSERT INTO users
            (
                name,email,password,
                age,height,weight,goal
            )
            VALUES(?,?,?,?,?,?,?)
            """,
            (
                name,email,hashed,
                age,height,weight,goal
            ))

            conn.commit()

            flash("Registration Successful")

            return redirect("/login")

        except:
            flash("Email already exists")

        finally:
            conn.close()

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(
                user["password"],
                password):

            session["user_id"] = user["id"]

            return redirect("/")

        flash("Invalid Credentials")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


@app.route("/bmi", methods=["POST"])
def bmi():

    height = float(request.form["height"])
    weight = float(request.form["weight"])

    bmi = weight / ((height / 100) ** 2)

    return render_template(
        "index.html",
        bmi=round(bmi, 2)
    )


@app.route("/fitness_ai", methods=["POST"])
def fitness_ai():

    goal = request.form["goal"]

    if goal == "Weight Loss":

        answer = """
        Workout:
        15 Squats x3
        10 Pushups x3
        20 Jumping Jacks x3

        Meals:
        Oats
        Fruits
        Dal
        Vegetables
        """

    elif goal == "Muscle Gain":

        answer = """
        Workout:
        Pushups
        Lunges
        Planks

        Meals:
        Eggs
        Paneer
        Chicken
        Milk
        """

    else:

        answer = """
        Walk 30 mins daily
        Eat balanced diet
        Sleep 8 hours
        """

    return render_template(
        "index.html",
        response=answer
    )


if __name__ == "__main__":

    app.run(debug=True)