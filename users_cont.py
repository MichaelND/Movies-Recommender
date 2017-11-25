# Michael Wang
# October 29, 2017
# Users Controller

import cherrypy
import re, json
from _movie_database import _movie_database

class UserController(object):

	def __init__(self, myd):
		self.myd = myd

	def GET(self, key = None):
		output = {}

		if key is None:
			output['users'] = []
			for uid in self.myd.users:
				user = {}
				user['zipcode'] 	= self.myd.users[uid]['zipcode']
				user['age']			= self.myd.users[uid]['age']
				user['gender'] 		= self.myd.users[uid]['gender']
				user['occupation'] 	= self.myd.users[uid]['occupation']
				user['id'] 			= uid
				output['users'].append(user)
				output['result'] = 'success'
		else:
			key = int(key)
			user = self.myd.get_user(key)
			if user is None:
				output['result'] 		= 'error'
				output['message'] 		= 'key not found'
			else:
				output['zipcode'] 		= user['zipcode']
				output['age']			= user['age']
				output['gender'] 		= user['gender']
				output['occupation'] 	= user['occupation']
				output['id'] 			= key
				output['result'] 		= 'success'

		return json.dumps(output)

	def PUT(self, key):
		req = cherrypy.request.body.read().decode()
		req = json.loads(req)

		key = int(key)
		output = {}

		try:
			info = {}
			info['zipcode'] 	= req['zipcode']
			info['age'] 		= req['age']
			info['gender'] 		= req['gender']
			info['occupation'] 	= req['occupation']
			self.myd.set_user(key, info)
			output['result'] 	= 'success'
		except KeyError:
			output['result'] 	= 'error'
			output['message'] 	= 'invalid request'

		return json.dumps(output)

	def POST(self):
		req = cherrypy.request.body.read().decode()
		req = json.loads(req)

		output = {}

		try:
			info = {}
			info['zipcode'] 	= req['zipcode']
			info['age'] 		= req['age']
			info['gender'] 		= req['gender']
			info['occupation'] 	= req['occupation']
			uid = self.myd.get_id("uid")
			self.myd.set_user(uid, info)
			output['result'] 	= 'success'
			output['id'] 		= uid
		except KeyError:
			output['result'] 	= 'error'
			output['message'] 	= 'invalid request'

		return json.dumps(output)

	def DELETE(self, key = None):
		output = {}
		if key is None:
			self.myd.users = {}
			output['result'] = 'success'
		else:
			key = int(key)
			try:
				del self.myd.users[key]
				output['result'] = 'success'
			except KeyError:
				output['result'] = 'error'
				output['message'] = 'key not found'

		return json.dumps(output)

	
