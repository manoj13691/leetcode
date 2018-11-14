#https://www.youtube.com/watch?v=nqlNzOcnCfs

def subset_sum(arr, total):
	mem = {}
	print(get_no_of_subsets(arr, total, len(arr)-1 ))
	print(get_no_of_subsets_dp(arr, total, len(arr)-1, mem))


# def get_no_of_subsets(arr, total, i):
# 	if i <0:
# 		return 0

# 	elif total <0:
# 		return 0

# 	elif total == 0:
# 		return 1

# 	elif total < arr[i]:
# 		return get_no_of_subsets(arr, total, i-1)

# 	else:
# 		return get_no_of_subsets(arr, total, i-1) + get_no_of_subsets(arr, total - arr[i], i-1)

def get_no_of_subsets(arr, total, i):
	if total==0:
		return 1

	elif total <0:
		return 0

	elif i<0:
		return 0

	elif total < arr[i]:
		return get_no_of_subsets(arr, total, i-1)

	else:
		return get_no_of_subsets(arr, total, i-1) + get_no_of_subsets(arr, total - arr[i], i-1)



def get_no_of_subsets_dp(arr, total, i, mem):
	key = str(total) +":"+ str(i)

	if key in mem:
		return mem[key]

	if total == 0:
		return 1

	elif total <0:
		return 0

	elif i<0:
		return 0

	elif total < arr[i]:
		value = get_no_of_subsets_dp(arr, total, i-1, mem)

	else:
		value = get_no_of_subsets_dp(arr, total, i-1, mem) + get_no_of_subsets_dp(arr, total - arr[i], i-1, mem)

	mem[key] = value
	return mem[key]





subset_sum([2,4,6,10], 16)
subset_sum([1,2,3], 3)

