#quick sort

# Quick Sort Exercise
def quickSort(l):
    run.ctr += 1
    #lesser=[]
    #greater=[]
    #pivot = [l[0]]
    "REPLACE THIS CODE WITH YOUR quickSort METHOD"
    if len(l)<=1:
    	print l
    	return l
    else:
    	pivot = l[0]
    	lesser = quickSort([x for x in l[1:] if x < pivot])
    	greater = quickSort([x for x in l[1:] if x>= pivot])
    	print lesser, pivot, greater
    	return lesser+[pivot]+greater
# Take things from text box and prepare output
def run():
    run.ctr = 0
    outstring = ""
    text=raw_input('input some numbers here: ')
    numbers = map(int, text.split(' '))
    #print numbers
    outstring += "Sorted Numbers: " + str(quickSort(numbers))
    outstring += "<br>Recursions: " + str(run.ctr)
    print outstring
    return outstring

if __name__=='__main__':
	run()