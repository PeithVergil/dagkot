from google.appengine.api import users

import base

from models.dagkot import Dagkot
        
class Home(base.BaseRequestHandler):
    def get(self):
        dagkots = Dagkot.all()
        offset = 0
        limit = 10

        user = users.get_current_user()
        if user:
            dagkots = dagkots.filter('dagkot_author =', user).order('dagkot_date').run(offset=offset, limit=limit)
        else:
			dagkots = dagkots.order('dagkot_date').run(offset=offset, limit=limit)
        
        self.render_html('home/home.html', dagkots=dagkots)

class Dagkots(base.BaseRequestHandler):
	def _query(self):
		try:
			limit = int(self.request.GET['n'])
		except KeyError:
			limit = 10

		try:
			offset = int(self.request.GET['o'])

			if offset > 0:
				offset -= 1

			offset *= limit
		except KeyError:
			offset = 0

		user = users.get_current_user()
		if user:
		    dagkots = Dagkot.all().filter('dagkot_author =', user).order('dagkot_date').run(offset=offset, limit=limit)
		else:
		    dagkots = Dagkot.all().order('dagkot_date').run(offset=offset, limit=limit)

		self.render_html('home/dagkots.html', dagkots=dagkots)

	def get(self):
		self._query()

	def post(self):
		self._query()