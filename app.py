import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Get current directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create full path to tasks.txt
TASK_FILE = os.path.join(BASE_DIR, "tasks.txt")


def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def save_task(task):
    with open(TASK_FILE, "a") as f:
        f.write(task + "\n")


@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("home.html", tasks=tasks)


@app.route("/add", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":
        task = request.form.get("task")

        if task:
            save_task(task)

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
