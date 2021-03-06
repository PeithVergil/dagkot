import json

from google.appengine.ext import blobstore, db
from google.appengine.ext.webapp import blobstore_handlers

import base

from models.dagkot import Dagkot

class UploadImages(base.BaseRequestHandler):
	def get(self, dagkot_key):
		data = {
			'upload_url': blobstore.create_upload_url('/upload/handler/%s' % dagkot_key)
		}

		self.render_html('upload/upload.html', **data)

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self, dagkot_key):
		# Generate a new upload URL for every upload request.
		data = {
			'upload_url': blobstore.create_upload_url('/upload/handler/%s' % dagkot_key),
			'status'    : 'FAILED'
		}
		
		dagkot = Dagkot.get(dagkot_key)
		if dagkot:
			uploads = self.get_uploads('file')
			blobkey = str(uploads[0].key())

			dagkot.dagkot_pictures.append(blobkey)

			key = dagkot.put()
			if key:
				data['status'] = 'OK'
			else:
				data['message'] = 'Unable to update the dagkot with the new image.'
		else:
			data['message'] = 'Invalid dagkot key. No dagkot was found.'

		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps(data))