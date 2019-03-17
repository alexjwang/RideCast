import json, requests
from flask import Flask, render_template

url = 'https://api.foursquare.com/v2/venues/search'

app = Flask(__name__,
            static_url_path='',
            static_folder='',
            template_folder='')

params = dict (
    client_id = 'DQEMSIAJ5MRKQWRNHMYW10FRRYHO12WZWXBTJJT3JMNZXW3S',
    client_secret = 'K3QGPTDIQCKDYQKERSXRM2WS0SGCBUGZUNDX3SAQUKYCDPRL',
    v = '20180323',
    ll = '40.7243,-74.0018',
    query = 'coffee',
    limit = 1,
    radius = 250,
)
resp = requests.get(url = url, params=params)
data = json.loads(resp.text)
print(data)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='localhost')