import sys
import re

def countNameScoreUsingListComprehension(dataArray):
    totalScore = sum([(index+1)*sum([(ord(ch) - 64) for ch in dataString]) for index, dataString in enumerate(dataArray)])
    return totalScore

if __name__ == '__main__':        
    f = open(sys.argv[1], 'r')
    dataArray = re.findall(r'[A-Z]+', f.readline())
    dataArray.sort()
    print countNameScoreUsingListComprehension(dataArray)

