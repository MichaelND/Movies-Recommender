# Michael Wang
# November 12, 2017
# Javascript milestone

import cherrypy
from _movie_database import _movie_database
from movies_cont import MovieController
from users_cont import UserController
from recommend_cont import RecommendationController
from ratings_cont import RatingController
from reset_cont import ResetController
from options_cont import OptionController

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    myd = _movie_database()
    myd.load_users('ml-1m/users.dat')
    myd.load_movies('ml-1m/movies.dat')
    myd.load_ratings('ml-1m/ratings.dat')
    myd.load_images('ml-1m/images.dat')

    movie_controller = MovieController(myd)
    user_controller = UserController(myd)
    recommendation_controller = RecommendationController(myd)
    rating_controller = RatingController(myd)
    reset_controller = ResetController(myd)
    option_controller = OptionController()

    #movies
    dispatcher.connect('movie_get', '/movies/', controller = movie_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('movie_post', '/movies/', controller = movie_controller, action = 'POST', conditions = dict(method=['POST']))
    dispatcher.connect('movie_delete', '/movies/', controller = movie_controller, action = 'DELETE', conditions = dict(method=['DELETE']))
    
    #movies:key
    dispatcher.connect('movie_get_key', '/movies/:key', controller = movie_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('movie_put_key', '/movies/:key', controller = movie_controller, action = 'PUT', conditions = dict(method=['PUT']))
    dispatcher.connect('movie_delete_key', '/movies/:key', controller = movie_controller, action = 'DELETE', conditions = dict(method=['DELETE']))

    #users
    dispatcher.connect('user_get', '/users/', controller = user_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('user_post', '/users/', controller = user_controller, action = 'POST', conditions = dict(method=['POST']))
    dispatcher.connect('user_delete', '/users/', controller = user_controller, action = 'DELETE', conditions = dict(method=['DELETE']))
    
    #users:key
    dispatcher.connect('user_get_key', '/users/:key', controller = user_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('user_put', '/users/:key', controller = user_controller, action = 'PUT', conditions = dict(method=['PUT']))
    dispatcher.connect('user_delete_key', '/users/:key', controller = user_controller, action = 'DELETE', conditions = dict(method=['DELETE']))

    #Recommendataions
    dispatcher.connect('recommendation_delete', '/recommendations/', controller = recommendation_controller, action = 'DELETE', conditions = dict(method=['DELETE']))
    dispatcher.connect('recommendation_get_key', '/recommendations/:key', controller = recommendation_controller, action = 'GET', conditions = dict(method=['GET']))
    dispatcher.connect('recommendation_put_key', '/recommendations/:key', controller = recommendation_controller, action = 'PUT', conditions = dict(method=['PUT']))

    #Ratings
    dispatcher.connect('rating_get_key', '/ratings/:key', controller = rating_controller, action = 'GET', conditions = dict(method=['GET']))

    #Reset
    dispatcher.connect('reset_put', '/reset/', controller = reset_controller, action = 'PUT', conditions = dict(method=['PUT']))
    dispatcher.connect('reset_put_key', '/reset/:key', controller = reset_controller, action = 'PUT', conditions = dict(method=['PUT']))

    #Connect
    dispatcher.connect('movie_option', '/movies/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('movie_option_key', '/movies/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('user_option', '/users/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('user_option_key', '/users/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('recommendations_option', '/recommendations/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('recommendations_option_key', '/recommendations/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('rating_option_key', '/ratings/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))
    dispatcher.connect('reset_option', '/reset/', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))    
    dispatcher.connect('reset_option_key', '/reset/:key', controller = option_controller, action = 'OPTIONS', conditions = dict(method=['OPTIONS']))

    #set up server
    conf = {'global':
                {'server.socket_host': 'student04.cse.nd.edu',
                'server.socket_port': 51080},
            '/': {'request.dispatch': dispatcher,
		  'tools.CORS.on': True} }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
