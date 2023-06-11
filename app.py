from flask import Flask, render_template
from flask_pymongo import pymongo
from dotenv import load_dotenv
from main.Routes import route
from user.UserModel import UserModel


import os
import flask_login

# setting static file path
app = Flask(__name__, static_folder='static', static_url_path='/static')

# loading environment variables
load_dotenv()

# connect to the database
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
cxn = pymongo.MongoClient(os.getenv('MONGO_URI'), serverSelectionTimeoutMS=5000)
try:
    cxn.admin.command('ping')
    db = cxn[os.getenv('MONGO_DBNAME')]
    print(' *', 'Connected to MongoDB!')
except Exception as e:
    print(' *', "Failed to connect to MongoDB at", os.getenv('MONGO_DBNAME'))
    print('Database connection error:', e)


# configuring flask-login
app.secret_key = os.getenv('SECRET_KEY')
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'route.login'


# registering routes
app.register_blueprint(route)


@login_manager.user_loader
def load_user(user_id):
    """To load user."""
    from main.Database import Database
    from flask import current_app
    from bson import ObjectId

    db = Database(current_app)
    objInstance = ObjectId(user_id)
    user_data = db.find_one("users", {"_id": objInstance})
    user = UserModel(
        user_data.get('email'),
        user_data.get('password'),
        user_data.get('username'),
        user_data.get('is_admin'),
    )
    if user:
        return user
    else:
        return None


# error handling
@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
