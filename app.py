import json
from flask import Flask
from myapp import MyApp

app = Flask(__name__)


@app.route('/')
def main_page():
    """
    welcome page
    :return:
    """
    return "Welcome to my world!"


@app.route('/list/')
def person_list():
    """
    to get users list
    :return: json of users list
    """
    application = MyApp()
    return json.dumps(application.get_persons_list())


@app.route('/interests/<user_id>')
def interests(user_id):
    """
    to get interesting events by user interests
    :param user_id: id of person
    :return: list of events
    """
    application = MyApp()
    return json.dumps(application.get_recommended(user_id, limit=60))


if __name__ == '__main__':
    app.run()