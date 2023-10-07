from chalice import Chalice
from flask import Flask, request, jsonify
import requests

app = Chalice(app_name='youtube-comments-api')

app = Flask(__name__)

# Base URL for the existing API
BASE_API_URL = "https://app.ylytic.com/ylytic/test"



@app.route('/search', methods=['GET'])
def search_comments():
    # Fetch parameters from the query string
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Build the query parameters for the existing API
    api_params = {}

    if search_author:
        api_params['author'] = search_author

    if at_from:
        api_params['at_from'] = at_from

    if at_to:
        api_params['at_to'] = at_to

    if like_from:
        api_params['like_from'] = like_from

    if like_to:
        api_params['like_to'] = like_to

    if reply_from:
        api_params['reply_from'] = reply_from

    if reply_to:
        api_params['reply_to'] = reply_to

    if search_text:
        api_params['search_text'] = search_text

    # Make a request to the existing API with the query parameters
    response = requests.get(BASE_API_URL, params=api_params)

    if response.status_code == 200:
        # Return the response from the existing API as-is
        return jsonify(response.json())
    else:
        # Handle errors as needed
        return jsonify({"error": "Failed to fetch comments from the existing API."}), 500


# Add additional Chalice configurations as needed

if __name__ == '__main__':
    app.debug = True
    app.run()



