def binarySearch(arr, val):
    lo = 0
    hi = len(arr)-1
    ctr = 0

    #REPLACE THIS CODE WITH YOUR binarySearch METHOD
    while lo <= hi:
    	mid = (lo+hi)/2
    	ctr += 1
    	print 'mid is ', mid
    	if arr[mid] < val:
    		lo = mid+1
    		print 'low is',lo
    	elif arr[mid] > val:
    		hi = mid-1
    		print 'high is ', hi
    	else:
    		print arr[mid], ctr
    		#return(mid, ctr)

	print "not found"
	return (-1, ctr)

def main():
	binarySearch([1,2,3,5,6,7], 1)


if __name__ =="__main__":
	main()