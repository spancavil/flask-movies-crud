from flask import Flask
from config import config
from flask_cors import CORS

#Import routes
from routes import Movie

app = Flask(__name__ )

CORS(app, resources={"*": {"origins": "*"}})

def page_not_found(error):
    return '<h1>Not found!</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #Blueprints
    #url_prefix es el prefijo de la url de Movie
    app.register_blueprint(Movie.main, url_prefix='/api/movies')

    #Error handler
    app.register_error_handler(404, page_not_found)
    app.run()