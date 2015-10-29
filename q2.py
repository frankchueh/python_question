with open("file.txt",'r') as f:
	first, second, third = 0, 0, 0
	for line in f:
		num = int(line)
		if num > first:
			first, second, third = num, first, second
		elif num > second:
			second, third = num, second
		elif num > third:
			third = num

	print first
	print second
	print third
	
