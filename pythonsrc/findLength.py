def findWidth():
	#userInput = input('What file do you want to search? ')
	userInput = 'v3.2.2GEOMETRY.geo'

	file = open(userInput,'r',encoding='cp1252')

	vertices = []
	for line in file:
		if line[0] not in '[;CPA ' and line != '\n':
			vertices += [list(map(float,line[1:].split()))]
	for point in vertices:
		for item in point:
			if item < 0:
				item *= -1
			
	small = float('inf')
	big = float('-inf')
	for point in vertices:
		if point[0] > big:
			big = point[0]
		if point[0] < small:
			small = point[0]

	file.close()

	#print(big)
	#print(small)
	#print(big-small)
	return big - small
print(findWidth())