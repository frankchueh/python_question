with open("file.txt",'r') as f:
	
	nums = [int(line) for line in f]
	list_num = []
	for n in range(1,5):
		max_num = 0
		for num in nums:
			if num > max_num:
				if num not in list_num:
					max_num = num
		print max_num
		list_num.insert(n,max_num)

