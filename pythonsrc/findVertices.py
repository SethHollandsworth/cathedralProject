import re
import codecs


def findVertices():
	#userInput = input('What file do you want to search? ')
	userInput = 'sound model v3.obj'

	file = codecs.open(userInput,'r','cp1252')

	vertices = []
	for line in file:
		if line[0:2] == 'v ':
			vertices += [list(map(float,line[1:].split()))]
	for point in vertices:
		if point[2] < 0:
			point[2] *= -1

	file.close()

	print(vertices)
findVertices()