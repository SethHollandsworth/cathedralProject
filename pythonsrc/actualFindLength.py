def findLength():
	#userInput = input('What file do you want to search? ')
	#userInput = 'churchTestLowCubeNormalizedFlippedYZ.geo'
	userInput = 'v3.2.2GEOMETRYBIGGERCHOIR.GEO'
	file = open(userInput,'r',encoding='cp1252')

	vertices = []
	for line in file:
		if line[0] not in '[;CPA ' and line != '\n':
			vertices += [list(map(float,line.split()))]
	#print(vertices)
	small = float('inf')
	big = float('-inf')
	for point in vertices:
		if point[1] > big:
			big = point[1]
		if point[1] < small:
			small = point[1]

	file.close()

	# print(big)
	# print(small)
	# print(big-small)
	return big - small
print(findLength())