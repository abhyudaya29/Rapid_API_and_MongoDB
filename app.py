import requests
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v4/get-statistics"

querystring = {"symbol": "AMRN", "region": "US", "lang": "en-US"}

headers = {
    "X-RapidAPI-Key": "eacd76d626msh0387a0d88f5f90ep1606e7jsnedea361af0ce",
    "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()

    # Save the response data in a JSON file
    with open("stock_data.json", "w") as json_file:
        json.dump(response_data, json_file, indent=4)

    print("API response saved in 'stock_data.json'")
else:
    print("API request failed with status code:", response.status_code)

uri = "mongodb+srv://abhyudaya:ab123@movie.9qlkub6.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["movie"]  # Replace with your database name
collection = db["abhyudaya"]
# Create a new client and connect to the server

collection.insert_one(response_data)
