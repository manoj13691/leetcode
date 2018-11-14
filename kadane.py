def max_sum_subarray(a):
	max_sum = a[0]
	global_max_sum = a[0]
	for i in range(1, len(a)):
		max_sum = max(a[i], max_sum + a[i])
		if max_sum > global_max_sum:
			global_max_sum = max_sum

	return global_max_sum

print(max_sum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))