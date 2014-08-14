



def saddle_points(matrix):
	matrix=matrix
	if len(matrix) <1:
		return set()
	testinput(matrix)
	row=[]
	column=[]
	result=[]
	i=j=0
	trans = zip(*matrix)
	for ele in matrix:
		row.append([i,index(max(ele)),ele])
		i+=1
	for ele in trans:
		column.append([index(min(ele),ele),j])
		j+=1
	print '+++'
	print row
	print column
	print '+++'
	for index in row:
		if index in column:
			result.append(tuple(index))
			#return index
	print '+++'
	print set(result)
	return set(result)

def testinput(matrix):

	set1=set()
	set1.add(len(matrix[0]))
	for ele in matrix:
		if len(ele) not in set1:
			raise ValueError, "input is not matrix"
	return

def index(num, list):
	