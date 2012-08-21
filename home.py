from google.appengine.api import users

import base

from models.dagkot import Dagkot
        
class Home(base.BaseRequestHandler):
    def get(self):
        data = {}

        limit = 10
        offset = 0

        user = users.get_current_user()
        if user:
            data['dagkots'] = Dagkot.all().filter('dagkot_author =', user).order('-dagkot_date').run(offset=offset, limit=limit)
        else:
            data['dagkots'] = Dagkot.all().order('-dagkot_date').run(offset=offset, limit=limit)
        
        self.render_html('home/home.html', **data)

class Dagkots(base.BaseRequestHandler):
	def get(self):
		try:
			limit = int(self.request.GET['n'])
		except KeyError:
			limit = 10

		try:
			offset = int(self.request.GET['o'])

			if offset > 1:
				offset = (offset - 1) * limit
			else:
				offset = 0
		except KeyError:
			offset = 0

		user = users.get_current_user()
		if user:
		    dagkots = Dagkot.all().filter('dagkot_author =', user).order('-dagkot_date').run(offset=offset, limit=limit)
		else:
		    dagkots = Dagkot.all().order('-dagkot_date').run(offset=offset, limit=limit)

		self.render_html('home/dagkots.html', dagkots=dagkots)