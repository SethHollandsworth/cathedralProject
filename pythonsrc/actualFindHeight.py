def findHeight():
	# userInput = input('What file do you want to search? ')
	userInput = 'v3.2.2GEOMETRYBIGGERCHOIR.GEO'

	file = open(userInput,'r',encoding='cp1252')

	vertices = []
	for line in file:
		if line[0] not in '[;CPA ' and line != '\n':
			vertices += [list(map(float,line.split()))]
	for point in vertices:
		#print(point)
		if point[3] < 0:
			point[3] *= -1
	small = float('inf')
	big = float('-inf')
	for point in vertices:
		if point[3] > big:
			big = point[3]
		if point[3] < small:
			small = point[3]
		#print(big,small)

	file.close()

	#print(big)
	#print(small)
	#print(big-small)
	return big - small
print(findHeight())