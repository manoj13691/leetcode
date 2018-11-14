#n-th Fibonacci number
def fib_bottom_up(n):
	if n ==1 or n==2:
		return 1

	else:
		dp_array = [None] * (n+1)
		dp_array[1] = 1
		dp_array[2] = 1

		for i in range(3, n+1):
			dp_array[i] = dp_array[i-1] + dp_array[i-2]

		return dp_array[n]


print(fib_bottom_up(100))
print(fib_bottom_up(10000))