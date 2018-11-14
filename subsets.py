# def all_subsets(given_array):
# 	subset = [None]*len(given_array)
# 	helper(given_array, subset, 0)

# def helper(given_array, subset, i):
# 	if i == len(given_array):
# 		#print(subset)
# 		temp = []
# 		for j in subset:
# 			if j!=None:
# 				temp.append(j)
# 		print(temp)

# 	else:
# 		subset[i] = None
# 		helper(given_array, subset, i+1)
# 		subset[i] = given_array[i]
# 		helper(given_array, subset, i+1)

# all_subsets([1,2,3])


def all_subsets(given_array):
	subset = [None]*len(given_array)
	print(helper(given_array, subset, 0, []))

def helper(given_array, subset, i, final_ans):
	if i == len(given_array):
		#print(subset)
		temp = []
		for j in subset:
			if j!=None:
				temp.append(j)
		final_ans.append(temp)

	else:
		subset[i] = None
		helper(given_array, subset, i+1, final_ans)
		subset[i] = given_array[i]
		helper(given_array, subset, i+1, final_ans)
	return final_ans

all_subsets([1,2,3])