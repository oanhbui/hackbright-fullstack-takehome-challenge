from flask import (Flask, render_template, request, session, redirect, flash)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = 'Something is wrong'
    response.content_type = "application/json"
    return response

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def login_user():
    user_name = request.form.get("username")
    user = crud.get_user_by_name(user_name)
    if user:
        session['user'] = user.user_id
        flash('login successful')
    else:
        flash('login failed!')
    return redirect('/')

@app.route('/slots', methods=['POST'])
def slot_list():
    choosen_date = request.form.get("date")
    choosen_start = request.form.get("start_time")
    choosen_end = request.form.get("end_time")
    return render_template("slots.html", date=choosen_date, start=choosen_start, end=choosen_end)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)