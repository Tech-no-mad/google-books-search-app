from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = 'AIzaSyDAJNLXB9kzX6rbViUKmV6uXGGQrgUfMbw' # replace with your API key

@app.route('/', methods=['GET', 'POST'])
def index():
    books = None
    error = None
    
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            base_url = 'https://www.googleapis.com/books/v1/volumes'
            params = {
                'q': query,
                'key': API_KEY
            }
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                books = response.json().get('items', [])
            else:
                error = "Failed to fetch data."
        else:
            error = "No query provided."
    
    return render_template('index.html', books=books, error=error)

if __name__ == '__main__':
    app.run(debug=True)
