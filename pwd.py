# PWD Generator

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"

pw_length = 6



def main():
	mypw = ""
	for i in range(pw_length):
		next_index = random.randrange(len(alphabet))
		mypw = mypw + alphabet[next_index]
	print mypw
	u = random.randrange(upper)
	n = random.randrange(num)
	

if __name__ == '__main__':
	main()