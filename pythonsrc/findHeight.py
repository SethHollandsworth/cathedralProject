def findWidth():
	#userInput = input('What file do you want to search? ')
	userInput = 'churchTestLowCubeNormalizedFlippedYZ.geo'

	file = open(userInput,'r',encoding='cp1252')

	vertices = []
	for line in file:
		if line[0] not in '[;CPA ' and line != '\n':
			vertices += [list(map(float,line[1:].split()))]
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
print(findWidth())