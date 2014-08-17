# test list as argv

def main(num,lists):
	result=[]
	#lists= [lists]
	print num,lists
	print lists.index(num)
	while num in lists:
		i=lists.index(num)
		result.append(i)
		lists.remove(num)
		lists.insert(i,num-1)
	print result,'result is here'


if __name__ =='__main__':
	num = 5
	lists = [3,2,4,5,6,5]
	main(num,lists)