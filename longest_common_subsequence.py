#https://www.youtube.com/watch?v=Qf5R-uYQRPk

def lcssHelper(s, t, m, n, mem):
	if m < 0 or n < 0:
		result = 0

	elif mem[m][n]!=None:
		return mem[m][n]

	elif s[m] == t[n]:
		result =  1 + lcssHelper(s, t, m-1, n-1, mem)

	else:
		result =  max(lcssHelper(s, t, m-1, n, mem), lcssHelper(s, t, m, n-1, mem))

	mem[m][n] = result
	return result

def lcss(s, t, m, n):
	mem = [[None for i in range(n)] for j in range(m)]
	#print(mem)
	return lcssHelper(s, t, m-1, n-1, mem)


a = "AGGTAB"
b = "GXTXAYB"
print(lcss(a, b, len(a), len(b)))