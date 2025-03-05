from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "51f991cc2fd0e48bb6a769c7e4d83e62"
API_URL = "https://api.marketstack.com/v1/eod"

def fetch_stock_data(symbol):
    querystring = {"access_key": API_KEY, "symbols": symbol}
    response = requests.get(API_URL, params=querystring)
    
    if response.status_code == 200:
        data = response.json().get("data", [])
        return data  # Returns a list of dictionaries
    else:
        return []

@app.route('/')
def index():
    stock_data = fetch_stock_data("AAPL")  # Fetch data for Apple stock
    return render_template("index.html", stock_data=stock_data)

if __name__ == "__main__":
    app.run(debug=True)
