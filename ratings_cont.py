# Michael Wang
# October 29, 2017
# Ratings Controller

import cherrypy
import re, json
from _movie_database import _movie_database

class RatingController(object):
	
	def __init__(self, myd):
		self.myd = myd

	def GET(self, key):
		output = {}
		key = int(key)
		output['movie_id'] = key
		output['rating'] = self.myd.get_rating(key)
		output['result'] = 'success'
		return json.dumps(output)