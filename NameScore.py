import sys

def countNameScore(dataArray):
    totalScore = 0
    i = 1
    for dataString in dataArray:
        dataStringScore = 0
#        print "-------------------------"
        for ch in dataString:
            dataStringScore += (ord(ch) - 64)
#            print ord(ch)-64
        dataStringScore *= i
        totalScore += dataStringScore
#        print "dataStringScore:%s" %(dataStringScore)
        i+=1
    return totalScore

f = open(sys.argv[1], 'r')
readData = f.readline()
readData = readData.strip()
readData = readData.replace("\"","")
dataArray = readData.split(",")
dataArray.sort()

print countNameScore(dataArray)

