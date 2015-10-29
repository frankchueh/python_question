with open("file3.txt") as f:

	names = [ line.strip('"') for line in f.readline().split(',') ]
	sorted_names = sorted(names)
	name_score, index = 0, 0

	for item in sorted_names:
		index += 1
		for letter in item:
			name_score += (ord(letter)-64)*index
			
	print(name_score)