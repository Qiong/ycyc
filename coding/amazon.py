#!/bin/python

##find the first character of the input string, which the character only appear once in the string

def main():
	string = raw_input("please put your string here:  ")
	count = {}
	lists = []
	for i in string:
		if i in count.keys() and count[i] == 1:
			count[i]= count[i]+1
			lists.pop(lists.index(i))
		elif i in count.keys() and count[i] >1:
			continue
		else:
			count[i]=1
			lists.append(i)

	if len(lists)>0 :		
		print "Found",lists[0]
	else: 
		print "Nothing Found !"
#	print lists
	#print lists, count
#	for ch in lists:
#		if count[ch] == 1 :
#			print 'Find the first character is:',ch
#			return
#		
#	print "No result found"


if __name__ == "__main__" :
	main()
