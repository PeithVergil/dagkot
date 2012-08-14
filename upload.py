import json

from google.appengine.api import images
from google.appengine.ext import blobstore, db
from google.appengine.ext.webapp import blobstore_handlers

import webapp2

import base

from models.dagkot import Dagkot, Photo

class UploadImages(base.BaseRequestHandler):
	def get(self, dagkot_key):
		data = {
			'upload_url': blobstore.create_upload_url('/upload/handler/%s' % dagkot_key)
		}

		self.render_html('upload/upload.html', **data)

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self, dagkot_key):
		data = {
			'upload_url' : blobstore.create_upload_url('/upload/handler/%s' % dagkot_key),
			'status'     : 'FAILED'
		}
		
		dagkot = Dagkot.get(dagkot_key)
		if dagkot:
			uploads = self.get_uploads('file')
			infokey = str(uploads[0].key())

			dagkot.dagkot_pictures.append(infokey)

			key = dagkot.put()
			if key:
				data['status'] = 'OK'

		# photo = Photo(photo_key=str(fileinfo.key()), photo_path=str(fileinfo), photo_dagkot=dagkot)
		# photo.put()

		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps(data))

# class ImageServe(base.BaseRequestHandler):
# 	def get(self, key):
# 		self.render_json({
# 		})
		
app = webapp2.WSGIApplication([
	('/upload/images/(.+)', UploadImages), ('/upload/handler/(.+)', UploadHandler)
], debug=True)