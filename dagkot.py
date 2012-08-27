from google.appengine.ext.db import BadKeyError

import base
from models.dagkot import Dagkot

class View(base.BaseRequestHandler):
	def get(self, dagkot_key):
		try:
			dagkot = Dagkot.get(dagkot_key)

			if dagkot:
				self.render_html('dagkot/view.html', dagkot=dagkot)
			else:
				message_cont = 'Dagkot does not exist'
				message_type = 'ERROR'

				self.render_html('home/landing.html',
					message_content=message_cont,
					message_type=message_type)
		except BadKeyError as e:
			message_cont = 'Invalid key'
			message_type = 'ERROR'

			self.render_html('home/landing.html',
				message_content=message_cont,
				message_type=message_type)