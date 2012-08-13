import json
import logging

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

import webapp2
from webapp2_extras import sessions

import base

from models.dagkot import Photo

class UploadHandlerTest(base.BaseRequestHandler):
	def get(self):
		config = sessions.default_config
		data = {
			'upload_url': blobstore.create_upload_url('/upload')
		}

		self.render_html('upload/test.html', **data)

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		# uploads = self.get_uploads('qqfile')
		#fileinfo = uploads[0]

		# photo = Photo(photo_key=fileinfo.key(), photo_path=str(fileinfo))
		# photo.put()

		# self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps({
			'success': True
			# 'key': str(fileinfo.key())
		}))



app = webapp2.WSGIApplication([
	('/upload/test', UploadHandlerTest), ('/upload', UploadHandler)
], debug=True)