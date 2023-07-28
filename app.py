from flask import Flask, render_template
from flask_pymongo import pymongo
from dotenv import load_dotenv
from main.Routes import route


import os

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


# registering routes
app.register_blueprint(route)


# error handling
@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
