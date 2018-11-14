#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

#Incomplete

def longest(data):
	# returns start index and length 
	if len(data) == 0:
		return -1, 0

	char_dict = dict()
	char_dict[data[0]] = 0

	max_len = 1
	max_start = 0

	cur_len = 1
	cur_start = 0

	for i in range(1, len(data)):
		char_dict[data[i]] = i

		if data[i] not in char_dict:
			cur_len +=1
			

		else:
			if cur_len > max_len:
				max_len = cur_len
				max_start = cur_start
				char_dict.clear()
			#cur_start = i+1
			cur_start = i
			cur_len = 1
			#cur_len = 1
			#char_dict.clear()

	if cur_len > max_len:
		max_len = cur_len


	print(data[max_start: max_start + max_len], max_len)

longest("abcabcbb")
longest("bbbbb")
longest("pwwkew")
longest("hello")
longest("dvdf")

    






