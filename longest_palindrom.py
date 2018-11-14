#https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

def longestPalindrome(data):
	data_length = len(data)
	mem = [[0 for i in range(data_length)] for j in range(data_length)]

	for i in range(data_length):
		mem[i][i] = 1

	max_length=1
	start = 0

	for i in range(data_length-1):
		if data[i] == data[i+1]:
			mem[i][i+1] = 1
			start = i
			max_length = 2

	#print(mem)


	for k in range(3, data_length+1):
		i =0
		while i<= data_length-k:
			j = i+k-1

			if mem[i+1][j-1]==1 and data[i] == data[j]:
				mem[i][j] = 1

				if k > max_length:
					max_length = k
					start = i
			i+=1

	return data[start:start+max_length]




data = "forgeeksskeegfor"
data = "babad"
print(longestPalindrome(data))