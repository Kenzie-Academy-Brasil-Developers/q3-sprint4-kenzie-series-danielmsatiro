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
    
    return serialized_serie, 201


def series():
    series = Series.read_series()
    print(series)
    
    serialized_series = [dict(zip(serie_columns, serie)) for serie in series]
    
    return jsonify(serialized_series), 200


def select_by_id(serie_id):
    return {"teste": "teste"}, 200
