import os
from jinja2 import Environment, FileSystemLoader

class Controller:
	def __init__(self):
		self.view_dir = os.path.join(os.getcwd(), 'views')
		
	def render_template(self, tpl, template_vars={}):
		env = Environment(loader = FileSystemLoader(self.view_dir))
		t = env.get_template(tpl)
		return t.render(template_vars)
