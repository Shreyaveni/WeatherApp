from flask import Flask, request, render_template
import requests

app = Flask(__name__)
API_KEY = "You_api_key"
BASE_URL = "  "

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        location = request.form['location']
        response = requests.get(f"{BASE_URL}?key={API_KEY}&q={location}&aqi=yes")
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "Invalid location or API issue."}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
