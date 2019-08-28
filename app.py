import json
import pickle
import requests
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

#load in data
listing_ids = pd.read_pickle('listing_data/dataframe_ids.pkl')

description_model = pickle.load(open('models/model101.pkl', 'rb'), encoding='latin1')
numerical_model = pickle.load(open('models/model102.pkl', 'rb'), encoding='latin1')

indices = pd.Series(listing_ids.index)
# print(indices)


app = Flask(__name__)

@app.route('/predict_desc', methods=['POST'])
def recommendation():

    similar_listings_id = []

    data = request.get_json(force=True)
    print(data)
    # print('loading data.....')

    idx = indices[indices == data['id']].index[0]
    # print(idx)
    score_series = pd.Series(description_model[idx]).sort_values(ascending=False)
    top_x_indexes = list(score_series.iloc[1:21].index)

    for i in top_x_indexes:
        similar_listings_id.append(list(listing_ids.i)[i])

    return jsonify(similar_listings_id)

@app.route('/predict_num', methods=['POST'])
def recommendation1():

    similar_listings_id = []

    data = request.get_json(force=True)
    print(data)
    # print('loading data.....')

    idx = indices[indices == data['id']].index[0]
    # print(idx)
    score_series = pd.Series(numerical_model[idx]).sort_values(ascending=False)
    top_x_indexes = list(score_series.iloc[1:21].index)

    for i in top_x_indexes:
        similar_listings_id.append(list(listing_ids.index)[i])

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
