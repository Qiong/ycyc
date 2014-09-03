import pickle

class Url(object):
	@classmethod
	def shorten(cls,full_url):
		"""shortens full url."""

		#Create an instance of Url class 
		instance = cls()
		instance.full_url=full_url
		instance.short_url=instance.create_short_url()
		Url.__save_url_mapping(instance)
		return instance