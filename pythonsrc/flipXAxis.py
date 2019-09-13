import codecs
import actualFindLength
def flipXAxis():
    xMax = actualFindLength.findLength()
    #yMin = 0
    #zMin = 3240.8
    #userInput = input('What file do you want to search? ')
    userInput = 'IN/scaledmodel_v6.GEO'

    file = open(userInput,'r',encoding='cp1252')
    vertFile = open('flippedXAxis.txt','w')
    
    count = 1
    for line in file:
        #print(line)
        if line[0] not in '[;CPA ' and line[0]:
            vertex = list(map(float,line.split()))
            print(vertex)
            if len(vertex) == 4:
                vertFile.write('%.0d %.3f %.3f %.3f\n' % (vertex[0], xMax - vertex[1], vertex[2], vertex[3]))
            #print(count, vertex[0] - xMin, vertex[1] - yMin, vertex[2] - zMin)
                count += 1
        else:
            vertFile.write(line)


    file.close()
    vertFile.close()


flipXAxis()