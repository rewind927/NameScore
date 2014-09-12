import sys
import re

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

def countNameScoreUsingListComprehension(dataArray):
    totalScore = sum([(index+1)*sum([(ord(ch) - 64) for ch in dataString]) for index, dataString in enumerate(dataArray)])
    return totalScore
        
f = open(sys.argv[1], 'r')
dataArray = re.findall(r'[A-Z]+', f.readline())
dataArray.sort()

print countNameScoreUsingListComprehension(dataArray)

