import typing as ty

from . import base

class LogChannel:
	"""Wrapper for log output.
	"""
	def __init__(self, sub):
		self.__sub = sub  # type: str
	
	def read_message(self):
		return next(self.__sub)
	
	def __iter__(self):
		return self.__sub
	
	def close(self):
		self.__sub.close()
	
	def __enter__(self):
		return self
	
	def __exit__(self, *a):
		self.close()

class Section(base.SectionBase):
	def log_tail(self,  **kwargs: base.CommonArgs):
		return LogChannel(self._client.request('/log/tail', decoder='json', stream=True))