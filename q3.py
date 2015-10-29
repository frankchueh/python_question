with open("file3.txt") as f:

	data = f.readline().strip('"').split('","')
	sorted_data = sorted(data)
	name_score, index = 0, 0

	for item in sorted_data:
		index += 1
		for letter in item:
			name_score += (ord(letter)-64)*index
			
	print(name_score)