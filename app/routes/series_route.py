from app.controllers import series_controller
from flask import Blueprint

bp = Blueprint("series", __name__, url_prefix="/series")

bp.post("")(series_controller.create)
bp.get("")(series_controller.series)
bp.get("/<int:serie_id>")(series_controller.select_by_id)

""" def series_route(app: Flask):
    @app.post("/series")
    def create():
        return {"teste": "teste"}, 201

    @app.get("/series")
    def series():
        return {"teste": "teste"}, 200

    @app.get("/series/<int:serie_id>")
    def select_by_id():
        return {"teste": "teste"}, 200 """
