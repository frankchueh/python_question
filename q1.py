def is_perfect(num):
	factors_sum = sum(factor for factor in range(1, num/2+1) if num%factor == 0)
	return factors_sum == num