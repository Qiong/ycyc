#enumerate

"""When looping through a sequence, the position index and corresponding value 
can be retrieved at the same time using the enumerate() function.

"""

# test list as argv

def main():


	for i, v in enumerate(['tic', 'tac', 'toe']):
		print i, v

	questions = ['name', 'quest', 'favorite color']
	answers = ['lancelot', 'the holy grail', 'blue']
	for q, a in zip(questions, answers):
		print 'What is your {0}?  It is {1}.'.format(q, a)


def saddle_points(rows):
    columns = [list(x) for x in zip(*rows)]

    if rows:
        len_first = len(rows[0])
        if any(len(row) != len_first for row in rows):
            raise ValueError('irregular matrix')

    result = set()
    for rownr, row in enumerate(rows):
        for posnr, pos in enumerate(row):
            if (pos == max(row) and
               pos == min(columns[posnr])):
                result.add((rownr, posnr))
    print "saddle_point_result_is"result
    return result




if __name__ =='__main__':
	inp = [[9,8,7],[5,3,2],[6,6,7]]
	main()
	saddle_points(inp)