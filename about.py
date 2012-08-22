import base

class About(base.BaseRequestHandler):
	def get(self):
		self.render_html('about/about.html')