from webapp2 import WSGIApplication

import settings

app = WSGIApplication(
	settings.routes,
	debug=settings.debug,
	config=settings.config
)