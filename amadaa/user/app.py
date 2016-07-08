import uuid
import amadaa.database
from amadaa.base import Model

class User(Model):
	def __init__(self, id=None):
		super().__init__()	
