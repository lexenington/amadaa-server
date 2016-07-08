import os
import uuid
from jinja2 import Environment, FileSystemLoader

class Controller:
	def __init__(self):
		self.view_dir = os.path.join(os.getcwd(), 'views')
		
	def render_template(self, tpl, template_vars={}):
		env = Environment(loader = FileSystemLoader(self.view_dir))
		t = env.get_template(tpl)
		return t.render(template_vars)
		
class Model:
	def __init__(self):
		self._attribs = { 'id': uuid.UUID }
		self.id = None
		
	def __getattr__(self, key):
		if key[0] == '_' or key in self._attribs:
			# XXX: don't really know why I need this here, but at times
			# I get stupid errors if I leave it out.
			try:
				return super.__getattr__(self, key)
			except:
				# TODO: appropriate exception class
				raise Exception("get: no such key")
		else:
			# TODO: appropriate exception class
			raise Exception("get: no such key")
			
	def __setattr__(self, key, value):
		if key[0] == '_':
			super.__setattr(self, key, value)
		elif key in self._attribs:
			if isinstance(value, self._attrib[key]) or value == None:
				super.__setattr__(self, key, value)
			else:
				# TODO: appropriate exception class
				raise Exception("set: incorrect value type")
		else:
			# TODO: appropriate exception class
			raise Exception("set: no such attribute")
			
	def save():
		if self.id == None:
			self._insert()
		else:
			self._update()
			
	def _insert():
		pass
		
	def _update():
		pass
