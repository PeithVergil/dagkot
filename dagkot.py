from google.appengine.api import users
from google.appengine.ext.db import BadKeyError

import base
import settings
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

class ViewAll(base.BaseRequestHandler):
	def get(self):
		limit = settings.DAGKOTS_PER_PAGE
		offset = 0
		dagkots = Dagkot.all().order('-dagkot_date').run(offset=offset, limit=limit)

		self.render_html('dagkot/view-all.html',
			dagkots=dagkots, current_page='ALL_DAGKOTS')

class ViewAllNext(base.BaseRequestHandler):
	def _query(self, page):
		limit = settings.DAGKOTS_PER_PAGE

		try:
			offset = int(page)
		except ValueError:
			offset = 0

		if offset > 0:
			offset -= 1

		offset *= limit

		dagkots = Dagkot.all().order('-dagkot_date').run(offset=offset, limit=limit)

		self.render_html('dagkot/view-all-next.html', dagkots=dagkots)

	def get(self, page):
		self._query(page)

	def post(self, page):
		self._query(page)

class ViewMine(base.BaseRequestHandler):
	def get(self):
		user = users.get_current_user()
		limit = settings.DAGKOTS_PER_PAGE
		offset = 0
		
		dagkots = Dagkot.all().filter('dagkot_author =', user).order('-dagkot_date').run(offset=offset, limit=limit)

		self.render_html('dagkot/view-mine.html',
			dagkots=dagkots, current_page='MY_DAGKOTS')

class ViewMineNext(base.BaseRequestHandler):
	def _query(self, page):
		user = users.get_current_user()
		limit = settings.DAGKOTS_PER_PAGE

		try:
			offset = int(page)
		except ValueError:
			offset = 0

		if offset > 0:
			offset -= 1

		offset *= limit

		dagkots = Dagkot.all().filter('dagkot_author =', user).order('-dagkot_date').run(offset=offset, limit=limit)

		self.render_html('dagkot/view-mine-next.html', dagkots=dagkots)

	def get(self, page):
		self._query(page)

	def post(self, page):
		self._query(page)