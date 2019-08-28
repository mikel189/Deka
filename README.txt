PROJECT TITLE

A recommender system for a real estate app

GETTING STARTED

-check the requirement.txt file for the necessary dependencies
-Use pip for installation

App.py: contains the the api that exposes endpoints to make a post request with an id of a listing
        return the description of related listings to that id.
        This could be tweaked to do a post request with description of a listing and get related listings as per their                 discription.
        
Request.py: Using the request module to make a post request to our endpoints

Models: This directory contails the two serialized models.
        One leveraging the description of listings 
        and the other using the other of listings, like bedrooms, bathrooms, etc.
        
Listings_data: Contains the serialized pikled and csv encoded type of our data.
