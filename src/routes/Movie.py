from flask import Blueprint, jsonify
from flask_parameter_validation import ValidateParameters, Route, Json
from datetime import datetime
import uuid

# Models
from models.MovieModel import MovieModel

# Entities
from models.entities.Movie import Movie

main = Blueprint('movie_blueprint', __name__)


@main.route('/')
def get_all_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_movie_by_id(id):
    try:
        movie = MovieModel.get_movie_by_id(id=id)
        if movie:
            return jsonify(movie)
        else:
            return jsonify({})
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/', methods=['POST'])
@ValidateParameters()
def add_movie(
    title: str = Json(min_str_length=5),
    duration: int = Json(min_int=10),
    released: datetime = Json()
):
    try:
        # request.json brings the body
        # print (request.json)

        # Must transform to string otherwise is an object
        id = str(uuid.uuid4())

        # title duration and released are validated with validation's library
        movie = Movie(id, title, duration, released)
        rows_affected = MovieModel.add_movie(movie)
        if rows_affected == 1:
            return jsonify(id)
        else:
            return jsonify({'message': 'No movie created'}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods=['PUT'])
@ValidateParameters()
def update_movie(
    id: str = Route(min_str_length=36, max_str_length=36),
    title: str = Json(min_str_length=5),
    duration: int = Json(min_int=10),
    released: datetime = Json()
):
    try:
        movie = Movie(id, title, duration, released)
        rows_affected = MovieModel.update_movie(movie)
        if rows_affected == 1:
            return jsonify(id)
        else:
            return jsonify({'message': 'No movie updated'}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>', methods=['DELETE'])
@ValidateParameters()
def delete_movie(
    id: str = Route(min_str_length=36, max_str_length=36),
):
    try:
        rows_affected = MovieModel.remove_movie_by_id(id)
        if rows_affected == 1:
            return jsonify(id)
        else:
            return jsonify({'message': 'No movie deleted'}), 400
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
