from flask import Blueprint, render_template, request, redirect
from main.UrlHandler import UrlHandler
from user.UserHandler import UserHandler
from flask_login import login_required


route = Blueprint('route', __name__)


@route.get('/')
# @login_required
def hello_world():
    return render_template('index.html')


@route.post('/')
# @login_required
def post_url():
    handler = UrlHandler()
    original_url = request.form['url']
    short_url = handler.post(original_url)
    return render_template('index.html', short_url=short_url)


@route.get('/<url_id>')
def redirect_to(url_id):
    handler = UrlHandler()
    original_url = handler.get(url_id)
    print(original_url)
    if original_url:
        return redirect(original_url)
    else:
        return render_template('index.html')


@route.post('/signup')
def signup():
    handler = UserHandler()
    r_data = request.json

    response = handler.signup(r_data)
    return response


@route.get('/login')
def login_page():
    return render_template('login.html')


@route.post('/login')
def login():
    handler = UserHandler()
    # r_data = request.json
    r_data = request.form

    response = handler.login(r_data)
    return redirect('/')
