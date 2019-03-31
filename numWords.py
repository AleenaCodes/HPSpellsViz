import re

inputFile = open("Books/Book1.txt.", 'r', encoding='utf8')
outputFile = open("Books/Book1Stripped.txt", 'w', encoding='utf8')

line = inputFile.readline()

while line:
    outputLine = re.sub('[^a-zA-Z0-9\n]', ' ', line)
    outputFile.write(outputLine)
    line = inputFile.readline()


wordsDict = {}

inputFile = open("Books/Book1Stripped.txt", 'r', encoding='utf8')

line = inputFile.readline()

lineNo = 0
while line:
    for word in line.split():
        if word in wordsDict:
            wordsDict[word]["total"] = (wordsDict[word]["total"] + 1)
            wordsDict[word]["lines"].append(lineNo)
        else:
            wordsDict[word] = {"total" : 1, "lines" : [lineNo]}
        # TODO need line here to add occurrence of word
    lineNo += 1
    line = inputFile.readline()

# iter = 0
# for key in sorted(wordsDict, key=wordsDict.get, reverse=True):
#   print("{} : {}".format(key,wordsDict[key]))
#   iter += 1
#   if (iter>20):
#       break

# sortedDict = sorted(wordsDict, key=wordsDict.get, reverse=True)
# print(sortedDict[0:20])
#
# sortedDict2 = sorted(wordsDict.values(), reverse=True)
# print(sortedDict2[0:20])

print("num of Wingardium is " + str(wordsDict["Alohomora"]))
