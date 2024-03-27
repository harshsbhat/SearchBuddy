from flask import Flask, request, jsonify, render_template
from search_buddy.search import main

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.form  # Get data from form submission
    keywords = data.get('keywords')
    array = data.getlist('array')

    if keywords is None or array is None:
        return jsonify({'error': 'Keywords and array parameters are required.'}), 400

    similar_array = main(keywords, array)
    return render_template('results.html', similar_array=similar_array)

if __name__ == '__main__':
    app.run(debug=True)
