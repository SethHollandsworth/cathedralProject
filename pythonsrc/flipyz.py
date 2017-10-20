import codecs
def flipyz():
    xMin = 4172.64
    yMin = 0
    zMin = 3240.8
    #userInput = input('What file do you want to search? ')
    userInput = 'churchTestLowCubeNormalized.geo'

    file = open(userInput,'r',encoding='cp1252')
    vertFile = open('verticesYZFlipped.txt','w')
    
    vertFile.write('Corners\n')
    count = 1
    for line in file:
        print(line)
        if line[0] not in '[;CPA ' and line[0]:
            vertex = list(map(float,line.split()))
            print(vertex)
            vertFile.write('%.0d %.3f %.3f %.3f\n' % (count, vertex[1], vertex[3], vertex[2]))
            #print(count, vertex[0] - xMin, vertex[1] - yMin, vertex[2] - zMin)
            count += 1


    file.close()
    vertFile.close()


flipyz()