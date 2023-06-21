from flask import Flask, render_template, request, redirect, url_for
import string
import random

app = Flask(__name__)

# Dictionary to store short URLs and their corresponding long URLs
url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('url')

    # Generate a random short URL
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))

    # Store the mapping between short URL and long URL
    url_mapping[short_url] = long_url

    short_url = url_for('redirect_to_long_url', short_url=short_url, _external=True)

    return render_template('shorten.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Invalid short URL."

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)
