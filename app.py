from flask import Flask, request, jsonify
from search_buddy.search import main

app = Flask(__name__)

@app.route('/search', methods=['POST'])  # Change method to POST
def search():
    data = request.json  # Get data from request body
    keywords = data.get('keywords')
    array = data.get('array')

    if keywords is None or array is None:
        return jsonify({'error': 'Keywords and array parameters are required.'}), 400

    similar_array = main(keywords, array)
    return jsonify({'similar_array': similar_array})

if __name__ == '__main__':
    app.run(debug=True)
