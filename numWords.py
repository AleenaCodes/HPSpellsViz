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

while line:
    for word in line.split():
        wordsDict[word] = wordsDict.get(word,0) + 1
    line = inputFile.readline()

iter = 0

for key in sorted(wordsDict, key=wordsDict.get, reverse=True):
  print("{} : {}".format(key,wordsDict[key]))
  iter += 1
  if (iter>20):
      break

# print("num of Wingardium is " + str(wordsDict["Wingardium"]))
