def uniqueChar(data):
	mem = {}

	for i in data:
		if i in mem:
			mem[i] +=1
		else:
			mem[i] = 1

	for i in range(len(data)):
		if mem[data[i]] == 1:
			return i

	return -1

print(uniqueChar("loveleetcode"))
