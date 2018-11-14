#https://www.youtube.com/watch?v=qli-JCrSwuk

def decode(data):
	print(helper(data, len(data)))

def helper(data, k):

	if k == 0:
		return 1 

	s = len(data) - k
	if data[s] == "0":
		return 0

	res = helper(data, k-1)

	if k >=2 and int(data[s:s+2]) <=26:
		res += helper(data, k-2)

	return res



def decodeDP(data):
	mem = [None] *  (len(data) + 1)
	print(helperDP(data, len(data), mem))


def helperDP(data, k, mem):

	if mem[k]!= None:
		return mem[k]

	if k == 0:
		return 1 

	s = len(data) - k
	if data[s] == "0":
		return 0

	res = helperDP(data, k-1, mem)

	if k >=2 and int(data[s:s+2]) <=26:
		res += helperDP(data, k-2, mem)

	mem[k] = res
	return res



decodeDP("1111111111111111111111111111111111111111")