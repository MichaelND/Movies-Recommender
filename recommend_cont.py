# Michael Wang
# October 29, 2017
# Recommendation Controller

import cherrypy
import re, json
from _movie_database import _movie_database

class RecommendationController(object):

	def __init__(self, myd):
		self.myd = myd

	def GET(self, key):
		output = {}
		key = int(key)
		recommendation = self.myd.get_highest_rated_unvoted_movie(key)
		if recommendation is None:
			output['result'] 	= 'error'
			output['message'] 	= 'key not found'

		output['result'] 	= 'success'
		output['movie_id'] 	= recommendation

		return json.dumps(output)

	def PUT(self, key):
		req = cherrypy.request.body.read().decode()
		req = json.loads(req)

		uid = int(key)
		output = {}

		try:
			mid 				= req['movie_id']
			rating 				= req['rating']
			result 				= self.myd.set_user_movie_rating(uid, mid, rating)
			output['result']	= 'success'
		except KeyError:
			output['result'] 	= 'error'
			output['message'] 	= 'invalid request'

		return json.dumps(output)

	def DELETE(self):
		output 			 = {}
		self.ratings 	 = {}
		output['result'] = 'success'

		return json.dumps(output)
