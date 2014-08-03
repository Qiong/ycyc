#wordcount

def word_count(string):
	count={}
	string = string.split()
	for char in string:
		if char in count.keys():
			count[char] = count[char]+1
		else:
			count[char] = 1
	print count
	return count
