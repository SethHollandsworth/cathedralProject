def findWidth():
	userInput = input('What file do you want to search? ')
	#userInput = 'churchTestLowCubeNormalizedFlippedYZ.geo'

	file = open(userInput,'r',encoding='cp1252')

	vertices = []
	for line in file:
		if line[0] not in '[;CPA ' and line != '\n':
			vertices += [list(map(float,line.split()))]
	for point in vertices:
		for item in point:
			if item < 0:
				item *= -1
			
	small = float('inf')
	big = float('-inf')
	for point in vertices:
		if point[2] > big:
			big = point[2]
		if point[2] < small:
			small = point[2]

	file.close()

	#print(big)
	#print(small)
	#print(big-small)
	return big - small
print(findWidth())