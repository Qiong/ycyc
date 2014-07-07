#!/usr/bin/python

#import math
def main():
	start = raw_input('please put integer here: ')
	past = set()
	while True:
		total = sum(int(i)**2 for i in str(start))
		print total
		if total ==1:
			print 'happy number'
			return
		if total in past:
			print 'Unhappy'
			return
		start = total
		past.add(total)


if __name__ == "__main__":
	main()