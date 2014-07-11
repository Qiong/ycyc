def binarySearch(arr, val):
    lo = 0
    hi = len(arr)-1
    ctr = 0

    #REPLACE THIS CODE WITH YOUR binarySearch METHOD
    while lo < hi:
    	mid = (lo+hi)/2
    	ctr += 1
    	if arr[mid] == val:
    		print mid, ctr    		
    		return mid, ctr
    	elif arr[mid] < val:
    		lo = mid+1
    		print lo
    	elif arr[mid] > val:
    		hi = mid-1
    		print hi

	print "not found"
	return (-1, ctr)

def main():
	binarySearch([1,2,3,4,5,6,7], 2)


if __name__ =="__main__":
	main()