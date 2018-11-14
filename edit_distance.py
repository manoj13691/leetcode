import sys

s1 = "gk"
s2 = "geeek"

s1 ="abcd"
s2 = "efgh"

s1 = "saturday"
s2 = "sunday"

s1 ="cat"
s2 = "cut"

s1 = "geek"
s2 = "gesek"

s1,s2 = sys.argv[1], sys.argv[2]

dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
#print dp

def edit(s1, s2 , i, j):

	if i>=len(s1) and j< len(s2):
		return 1 + edit(s1, s2, i, j+1)

	if i<len(s1) and j>=len(s2):
		return 1 + edit(s1, s2, i+1, j)

	if i >= len(s1) or j>= len(s2):
		return 0

	if s1[i] == s2[j]:
		return edit(s1, s2, i+1, j+1)


	return min((1 + edit(s1, s2, i, j+1)) , (1 + edit(s1, s2, i+1, j)), (1 + edit(s1, s2, i+1, j+1)))


print edit(sys.argv[1], sys.argv[2], 0, 0)


def editDP_top(s1, s2 , i, j):

	if i>=len(s1) and j< len(s2):

		if dp[i][j] == -1:
			dp[i][j] = 1 + edit(s1, s2, i, j+1)
		return dp[i][j]

	if i<len(s1) and j>=len(s2):

		if dp[i][j] == -1:
			dp[i][j] = 1 + edit(s1, s2, i+1, j)
		return dp[i][j]

	if i >= len(s1) or j>= len(s2):
		dp[i][j] = 0
		return dp[i][j]

	if s1[i] == s2[j]:
		if dp[i][j] == -1:
			dp[i][j] = edit(s1, s2, i+1, j+1)
		return dp[i][j]

	if dp[i][j] == -1:
		dp[i][j] = min((1 + edit(s1, s2, i, j+1)) , (1 + edit(s1, s2, i+1, j)), (1 + edit(s1, s2, i+1, j+1)))

	return dp[i][j]
	#return min((1 + edit(s1, s2, i, j+1)) , (1 + edit(s1, s2, i+1, j)), (1 + edit(s1, s2, i+1, j+1)))

#print editDP(s1, s2, 0, 0)


def editDP(s1, s2 , i, j):

	for i in range(len(s1)+1):
		for j in range(len(s2)+1):

			if i == 0:
				dp[i][j] = j

			elif j == 0:
				#print(i,j)
				dp[i][j] = i

			# if i>=len(s1) and j< len(s2):
			# 	dp[i][j] = len(s2) - j

			# if i<len(s1) and j>=len(s2):
			# 	dp[i][j] = len(s1) - i

			#if i >= len(s1) or j>= len(s2):
				#dp[i][j] = 0
				#return dp[i][j]

			elif s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]

			# if dp[i][j] == -1:
			# 	dp[i][j] = min((1 + edit(s1, s2, i, j+1)) , (1 + edit(s1, s2, i+1, j)), (1 + edit(s1, s2, i+1, j+1)))

			else:

				dp[i][j] = 1 + min( dp[i][j-1] , dp[i-1][j], dp[i-1][j-1])
			#return min((1 + edit(s1, s2, i, j+1)) , (1 + edit(s1, s2, i+1, j)), (1 + edit(s1, s2, i+1, j+1)))
	#print dp
	return dp[i][j]
#print editDP(s1, s2, 0, 0)