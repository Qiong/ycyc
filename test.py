

def main(string):
	string = string
    translate = dict(G='C', C='G', T='A', A='U')
    print ''.join(translate[char] for char in string)


if __name__ == '__main__':
	main('ACGTGGTCTTAA')