import requests
import os
import json
import flask
from flask import *
import datetime as dt

year = dt.datetime.today().year

API_KEY = os.environ["API_KEY"]
app = Flask(__name__)

url = "https://places.googleapis.com/v1/places:searchText"

def find_places(query):
    payload = {
        "textQuery": query
    }

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": (
            "places.id,"                 # <-- REQUIRED
            "places.displayName,"
            "places.formattedAddress,"
            "places.rating"
        )
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json().get("places", [])

def get_place_info(place_id):
    url = f"https://places.googleapis.com/v1/places/{place_id}"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        "X-Goog-FieldMask": (
            "id,"
            "displayName,"
            "formattedAddress,"
            "websiteUri,"
            "photos"
        )
    }

    response = requests.get(url, headers=headers)
    return response.json()

def build_photo_url(photo_name, max_width=400):
    return (
        f"https://places.googleapis.com/v1/{photo_name}/media"
        f"?maxWidthPx={max_width}&key={API_KEY}"
    )





@ app.route("/", methods=["GET"])
def index():
    search_query = request.args.get("query", "")
    query_results = find_places(search_query)
    results = []
    for p in query_results:
        place_id = p["id"]
        name = p["displayName"]["text"]
        address = p["formattedAddress"]
        rating = p.get("rating", "")
        details = get_place_info(place_id)

        website = details.get("websiteUri", "No website listed")

        photos = details.get("photos", [])
        if photos:
            photo_name = photos[0]["name"]
            photo_url = build_photo_url(photo_name)
        else:
            photo_url = "No photo available"
        place_entry = {
            "name": name,
            "address": address,
            "website": website,
            "photo_url": photo_url,
            "rating": rating
        }
        results.append(place_entry)
        results.sort(key=lambda x: x["rating"] or 0, reverse=True)


    return render_template("index.html",
                           results = results,
                           query = search_query,
                           year = year,)
@app.route("/about")
def about():

    return render_template("about.html",
                           year = year,)

@app.route("/contact", methods=["GET", "POST"])
def contact():

    return render_template("contact.html",
                           year = year,)



if __name__ == "__main__":
    app.run(debug=True)