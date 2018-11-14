def intersection(a,b):
	a_dict = {}
	intersection_set = []
	for i in a:
		a_dict[i] = 1
	for i in b:
		if i in a_dict:
			intersection_set.append(i)
	return intersection_set

print intersection([1,2,3,4],[5,6,7,8])
