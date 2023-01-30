from flask import Flask, render_template, request, redirect, url_for
import db
app = Flask(__name__)

@app.route("/",  methods = ["POST", "GET"])
def index():
    if request.method == 'POST':
        username = request.form.get('username', None)
        global current_user
        current_user = db.check_user(username)
        if (current_user != None):
            current_user = db.check_user(username)
            return redirect(url_for('home'))
        else:
            return render_template('index.html', error_message = "User does not exist. Please contact admin to add user.")
    return render_template('index.html')

@app.route("/home",  methods = ["POST", "GET"])
def home():
    return render_template('home.html')

@app.route("/event",  methods = ["POST", "GET"])
def event():
    lst = db.get_events(current_user)
    return render_template('event.html', list = lst)

@app.route("/task",  methods = ["POST", "GET"])
def task():
    lst = db.get_tasks(current_user)
    return render_template('task.html', list = lst)

@app.route("/create_event",  methods = ["POST", "GET"])
def create_event():
    return render_template('create_event.html')

@app.route("/create_task",  methods = ["POST", "GET"])
def create_task():
    return render_template('create_task.html')

if __name__ == "__main__":
    app.run(debug=True)