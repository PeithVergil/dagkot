import json

from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

import webapp2

import base

from models.dagkot import Photo

class UploadImages(base.BaseRequestHandler):
	def get(self, dagkot_key):
		data = {
			'upload_url': blobstore.create_upload_url('/upload/handler')
		}

		self.render_html('upload/upload.html', **data)

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		uploads = self.get_uploads('file')
		fileinfo = uploads[0]

		# photo = Photo(photo_key=fileinfo.key(), photo_path=str(fileinfo))
		# photo.put()

		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps({
			'upload_url' : blobstore.create_upload_url('/upload/handler'),
			'file_key'   : images.get_serving_url(fileinfo.key())
		}))

# class ImageServe(base.BaseRequestHandler):
# 	def get(self, key):
# 		self.render_json({
# 		})
		
app = webapp2.WSGIApplication([
	('/upload/images/(.+)', UploadImages), ('/upload/handler', UploadHandler)
], debug=True)