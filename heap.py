
A = [1,5,6,8,12,14,16]

A.reverse()

#From geeks for geeks

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    #print(l,r)
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 




def heapSort(arr): 
	n = len(arr) 

	# Build a maxheap. 
	for i in range(int(n/2), -1, -1): 
		heapify(arr, n, i)
		#print(arr)

	count = 0
	for i in range(n-1, -1, -1):
		#print(arr[0])
		arr[i], arr[0] = arr[0], arr[i] # swap 
		count+=1

		if count<k:
			heapify(arr, i, 0) 

		else:
			break

k = 4
heapSort(A)
print(A[-4:])

