import codecs
def normalize():
	xMin = 4172.64
	yMin = 0
	zMin = 3240.8
	#userInput = input('What file do you want to search? ')
	userInput = 'churchTestLowCube.geo'

	file = open(userInput,'r',encoding='cp1252')
	vertFile = open('vertices.txt','w')
	
	vertFile.write('Corners\n')
	count = 1
	for line in file:
		if line[0] not in '[;CPA ':
			vertex = list(map(float,line.split()))
			#print(vertex)
			vertFile.write('%.0d %.3f %.3f %.3f\n' % (count, vertex[1] - xMin, vertex[2] - yMin, vertex[3] - zMin))
			#print(count, vertex[0] - xMin, vertex[1] - yMin, vertex[2] - zMin)
			count += 1


	file.close()
	vertFile.close()


normalize()