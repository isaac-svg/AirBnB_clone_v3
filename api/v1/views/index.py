#!/usr/bin/python3
"""connect to API"""
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify


hbnbText = {
    "cities": "City",
    "users": "User",
    "places": "Place",
    "amenities": "Amenity",
    "states": "State",
    "reviews": "Review",
}


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """Returns a response object with status OK"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """computes the statistics of the  db"""
    return_dict = {}
    for key, value in hbnbText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)


if __name__ == "__main__":
    pass
