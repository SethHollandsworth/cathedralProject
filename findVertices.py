import re


def findVertices():
	#userInput = input('What file do you want to search? ')
	userInput = 'sound model v3.obj'
	file = open(userInput,'r')
	file.close()
	vertices = re.findall(r'v \d+ \d+ \d+',file)
	for vertex in vertices:
		print(vertex)