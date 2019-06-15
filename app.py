import json
import pickle
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

#load in data
df = pd.read_pickle('deka_data.pkl')

nearest_neighbor = pickle.load(open('model101.pkl', 'rb'))

indices = pd.Series(df.index)


app = Flask(__name__)

@app.route('/', methods=['POST'])
def recommendation():

    similar_listings_id = []

    data = request.get_json(force=True)
    # print(data)
    # print('loading data.....')

    idx = indices[indices == data].index[0]
    score_series = pd.Series(nearest_neighbor[idx]).sort_values(ascending=False)
    top_x_indexes = list(score_series.iloc[1:21].index)

    for i in top_x_indexes:
        similar_listings_id.append(list(df.index)[i])

    return jsonify(similar_listings_id)


if __name__ == '__main__':
    app.run(debug=True)
# def recommend(id_, nearest_neighbor = nearest_neighbor):
#
#     similar_listings_id = []
#
#     #getting the index of the listing that matches the id
#     idx = indices[indices == id_].index[0]
#
#     #creating a series with similarity score in descending order
#     score_series = pd.Series(nearest_neighbor[idx]).sort_values(ascending=False)
#
#     # getting the indexes of the 10 most similar listings except itself
#     top_10_indexes = list(score_series.iloc[1:11].index)
#
#     # populating the list with the ids of the top 10 matching similar_listings_id
#     for i in top_10_indexes:
#         similar_listings_id.append(list(df.index)[i])
#
#     return similar_listings_id
#
#
