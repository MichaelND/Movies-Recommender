# Michael Wang
# October 29, 2017
# Reset Controller

import cherrypy
import re, json
from _movie_database import _movie_database

class ResetController(object):

	def __init__(self, myd):
		self.myd = myd

	def PUT(self, key = None):
		output = {}

		if key is None:
			self.myd.load_users('ml-1m/users.dat')
			self.myd.load_movies('ml-1m/movies.dat')
			self.myd.load_ratings('ml-1m/ratings.dat')
			self.myd.load_images('ml-1m/images.dat')
			output['result'] = 'success'
		else:
			key = str(key)
			new_myd = _movie_database()
			new_myd.load_movies('ml-1m/movies.dat')
			try:
				self.myd.movies[key] = new_myd.get_movie(key)
				output['result'] 	 = 'success'
			except KeyError:
				output['result'] 	= 'error'
				output['message'] 	= 'invalid request'

		return json.dumps(output)
