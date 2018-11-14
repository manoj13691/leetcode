def pairSum(data, total):
	mem = {}

	ans = {} #To store unique pairs

	for i in data:
		mem[i] = "Present"

	for i in data:
		if total-i in mem:
			if (i, total-i) not in ans and (total-i, i) not in ans:
				ans[(i, total-i)] = "Present"

	print(len(ans))
	#for i in ans:
		#print(i)


pairSum([1, 2, 3, 6, 7, 8, 9, 1], 10)
