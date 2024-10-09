from flask import Flask, render_template, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os
import secrets

# Allow OAuth without HTTPS for local development
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('main'))
    return render_template('index.html')

@app.route('/login')
def login():
    nonce = secrets.token_urlsafe(16)
    session['nonce'] = nonce
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri, nonce=nonce)

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    nonce = session.pop('nonce', None)
    user_info = google.parse_id_token(token, nonce=nonce)
    session['user'] = user_info
    return redirect(url_for('main'))

@app.route('/main')
def main():
    if 'user' not in session:
        return redirect(url_for('index'))
    user = session['user']
    return render_template('main.html', email=user['email'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")
