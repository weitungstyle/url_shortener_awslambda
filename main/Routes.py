from flask import Blueprint, render_template, request, redirect
from main.UrlHandler import UrlHandler


route = Blueprint('route', __name__)


@route.get('/')
def hello_world():
    return render_template('index.html')


@route.post('/')
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
        if original_url.startswith('http://') or original_url.startswith('https://'):
            return redirect(original_url)
        else:
            return redirect(f'//{original_url}')
    else:
        return redirect('/')
