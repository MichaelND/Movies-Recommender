# Michael Wang
# October 29, 2017
# Movies Controller

import cherrypy
import re, json
from _movie_database import _movie_database

class MovieController(object):

    def __init__(self, myd):
        self.myd  = myd

    def GET(self, key = None):
        output = {}

        if key is None: 
            output['movies'] = []

            for mid in self.myd.movies:
                movie = {}
                movie['genres']     = self.myd.movies[mid]['genres']
                movie['title']      = self.myd.movies[mid]['title']
                movie['id']         = mid
                output['movies'].append(movie)

            output['result'] = 'success'
        else:
            key = int(key)
            m = self.myd.get_movie(key)
            if m is None:
                output['result']    = 'error'
                output['message']   = 'key not found'
            else:
                output['genres']    = m['genres']
                output['title']     = m['title']
                output['id']        = key
                output['result']    = 'success'
                output['img']       = self.myd.get_image(key)

        return json.dumps(output)

    def POST(self):
        req = cherrypy.request.body.read().decode()
        req = json.loads(req)
        output = {}

        try:
            info = {}
            info['title']  = req['title']
            info['genres'] = req['genres']
            mid = self.myd.get_id("mid")
            self.myd.set_movie(mid, info)
            output['result']    = 'success'
            output['id'] = mid
        except KeyError as ex:
            output['result']    = 'error'
            output['message']   = 'key not found'

        return json.dumps(output)

    def PUT(self, key):
        req = cherrypy.request.body.read().decode()
        req = json.loads(req)
        output = {}
        key = int(key)

        try:
            movie = {}
            movie['title']      = req['title']
            movie['genres']     = req['genres']
            self.myd.set_movie(key, movie);
            output['result'] = 'success'
        except KeyError as ex:
            output['result']    = 'error'
            output['message']   = 'key not found'

        return json.dumps(output)

    def DELETE(self, key = None):
        output = {}
        
        if key is None:
            self.myd.movies     = {}
            output['result']    = 'success'
        else:
            key = int(key)
            try:
                del self.myd.movies[key]
                output['result']    = 'success'
            except KeyError as ex:
                output['result']    = 'error'
                output['message']   = 'key not found'

        return json.dumps(output)
