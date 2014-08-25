

class Phone(object):
	"""docstring for Phone"""
	def __init__(self, number):
		#super(Phone, self).__init__()
		self.origin_number = number
		self.number = self.format_number()

	def format_number(self):
		result =''
		for i in self.origin_number:
			if i.isdigit():
				result=result+str(i)
		if len(result)<10:
			print'bad number'
			return
		if len(result)>10 and result[0]!=1:
			print'bad number'
			return
		else:
			return result
	
