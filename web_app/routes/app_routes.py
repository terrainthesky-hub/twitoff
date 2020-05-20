
from flask import Blueprint, jsonify, request, flash, redirect

from web_app.models import db, User, Tweet

app_routes = Blueprint("app_routes", __name__)

@app_routes.route('/')
def root():
    return render_template('base.html', title='Home', users=User.query.all(),
                               comparisons=CACHED_COMPARISONS)
@app_routes.route('/users', methods=['POST'])
@app_routes.route('/users/<name>', methods=['GET'])
def user(name=None, message=''):
    name = name or request.values['user_name']
    try:
        if request.method == 'POST':
            add_or_update_user(name)
            message = "User {} successfully added!".format(name)
        tweets = User.query.filter(User.name == name).one().tweets
    except Exception as e:
        message = "Error adding {}: {}".format(name, e)
        tweets = []
    return render_template('users.html', title=name, tweets=tweets,
                               message=message)
