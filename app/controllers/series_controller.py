from curses.ascii import HT
from http import HTTPStatus

from app.models.series_model import Series
from flask import jsonify, request

serie_columns = [
        "_id",
        "serie",
        "seasons"
        "released_date",
        "genre",
        "imdb_rating"
    ]

def create():
    payload = request.get_json()

    serie = Series(**payload)
    inserted_serie = serie.create_serie()
    
    serialized_serie = dict(zip(serie_columns,inserted_serie))
    
    return serialized_serie, HTTPStatus.CREATED


def series():
    series = Series.read_series()
    
    serialized_series = [dict(zip(serie_columns, serie)) for serie in series]
    
    return jsonify(serialized_series), HTTPStatus.OK


def select_by_id(serie_id):
    serie = Series.read_serie_by_id(serie_id)
    
    if serie:
        return dict(zip(serie_columns, serie)),200
    
    return {}, HTTPStatus.NOT_FOUND
