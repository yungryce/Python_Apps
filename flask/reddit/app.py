from flask import Flask, jsonify
import os
import requests

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/')
def get_reddit_data():
    auth = requests.auth.HTTPBasicAuth(os.getenv('CLIENT_ID'), os.getenv('SECRET_KEY'))

    data = {
        'grant_type': 'password',
        'username': 'chxgbx',
        'password': 'mv#Q9u&6SXK^G8Gqe4K8'
    }
    headers = {'User-Agent': 'test/api/v1'}
    req = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

    # Check if authentication was successful
    if req.status_code == 200:
        access_token = req.json()['access_token']
        headers['Authorization'] = f'bearer {access_token}'

        # Make a request to get user data
        user_req = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

        # Check if user data request was successful
        if user_req.status_code == 200:
            user_data = user_req.json()
            return jsonify(user_data)
        else:
            return jsonify({'error': 'Failed to fetch user data from Reddit API'}), user_req.status_code
    else:
        return jsonify({'error': 'Failed to authenticate with Reddit API'}), req.status_code

if __name__ == '__main__':
    app.run(debug=True)