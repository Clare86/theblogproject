import webapp2
import cgi
import re
import os
import jinja2
import time
import urllib2
import logging

from xml.dom import minidom
from google.appengine.api import memcache
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)


class BaseHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
		
	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)
		
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainHandler(BaseHandler):
    def get(self):
    	self.render("index.html")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
