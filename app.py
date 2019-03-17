import json, requests
from urllib.request import urlopen
from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='',
            template_folder='')

location = '40.7243,-74.0018'

url = 'https://api.foursquare.com/v2/venues/search'

params = dict (
    client_id = 'DQEMSIAJ5MRKQWRNHMYW10FRRYHO12WZWXBTJJT3JMNZXW3S',
    client_secret = 'K3QGPTDIQCKDYQKERSXRM2WS0SGCBUGZUNDX3SAQUKYCDPRL',
    v = '20180323',
    ll = location,
    query = 'coffee',
    limit = 1,
    radius = 250,
)
resp = requests.get(url = url, params=params)
foursqData = json.loads(resp.text)
print(foursqData)


tripData = json.load(urlopen("http://api.tripadvisor.com/api/partner/2.0/location/48739/?key=2f5aef9e-d399-4298-9986-ea6305c270a8"))
print(tripData)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='localhost')