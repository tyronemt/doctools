from flask import Flask, render_template, request, redirect, url_for, session
import db
import csv


app = Flask(__name__)
app.secret_key = "doc"

@app.route("/",  methods = ["POST", "GET"])
def index():
    if request.method == 'POST':
        username = request.form.get('username', None)
        session["current_user"] = db.check_user(username)
        if (session["current_user"] != None):
            session["current_user"] = db.check_user(username)
            return redirect(url_for('home'))
        else:
            return render_template('index.html', error_message = "User does not exist. Please contact admin to add user.")
    return render_template('index.html')

@app.route("/home",  methods = ["POST", "GET"])
def home():
    return render_template('home.html')

@app.route("/event",  methods = ["POST", "GET"])
def event():
    lst = db.get_events(session["current_user"])
    return render_template('event.html', list = lst)

@app.route("/task",  methods = ["POST", "GET"])
def task():
    lst = db.get_tasks(session["current_user"])
    return render_template('task.html', list = lst)

@app.route("/create_event",  methods = ["POST", "GET"])
def create_event():
    if request.method == 'POST':
        name = request.form.get('name', None)
        description = request.form.get('description', "")
        db.create_event(session["current_user"], name, description)
        return redirect(url_for('event'))
    return render_template('create_event.html')

@app.route("/create_task",  methods = ["POST", "GET"])
def create_task():
    if request.method == 'POST':
        name = request.form.get('name', None)
        description = request.form.get('description', "")
        due_date = request.form.get('due_date')
        db.create_task(session["current_user"], name, description, due_date)
        return redirect(url_for('task'))
    return render_template('create_task.html')

@app.route("/info",  methods = ["POST", "GET"])
def info():
    return render_template('info.html')

@app.route("/san_bernardino",  methods = ["POST", "GET"])
def san_bernardino():
    lst = []
    with open("static\san_bernardino.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return render_template('office.html', name = "San Bernardino Clinic", list = lst)

@app.route("/riverside",  methods = ["POST", "GET"])
def riverside():
    lst = []
    with open("static\-riverside.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return render_template('office.html', name = "Riverside Clinic", list = lst)

@app.route("/pomona",  methods = ["POST", "GET"])
def pomona():
    lst = []
    with open("static\pomona.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return render_template('office.html', name = "Pomona Clinic", list = lst)

@app.route("/montclair",  methods = ["POST", "GET"])
def montclair():
    lst = []
    with open("static\montclair.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return render_template('office.html', name = "Montclair Clinic", list = lst)

@app.route("/referral_codes",  methods = ["POST", "GET"])
def referral_codes():
    lst = []
    with open("static\-referral_codes.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return render_template('referral_codes.html', name = "Referral Codes", list = lst)

@app.route("/cpt_code",  methods = ["POST", "GET"])
def cpt_code():
    return render_template('cpt_code.html')


if __name__ == "__main__":
    app.run(debug=True)