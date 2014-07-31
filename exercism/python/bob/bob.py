#bob.py

import string

	#@classmethod
def hey(sentence):
	#interpreter = SentenceInterpreter(sentence)

	if sentence == '':
		return 'Fine. Be that way!'

	elif sentence.isupper():
		return 'Woah, chill out!'

	elif sentence.endswith('?') :
		return 'Sure.'
	else:
		return 'Whatever.'

