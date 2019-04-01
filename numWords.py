import re

wordsDict = {}
prevHarry = 0
nowHarry = 0

filesnames = ["Books/Book1Stripped.txt",
              "Books/Book2Stripped.txt",
              "Books/Book3Stripped.txt",
              "Books/Book4Stripped.txt",
              "Books/Book5Stripped.txt",
              "Books/Book6Stripped.txt",
              "Books/Book7Stripped.txt"]

shortNames = {"Books/Book1Stripped.txt": "1",
              "Books/Book2Stripped.txt": "2",
              "Books/Book3Stripped.txt": "3",
              "Books/Book4Stripped.txt": "4",
              "Books/Book5Stripped.txt": "5",
              "Books/Book6Stripped.txt": "6",
              "Books/Book7Stripped.txt": "7"}

for filename in filesnames:
    inputFile = open(filename, 'r', encoding='utf8')
    shortName = shortNames[filename]

    line = inputFile.readline()

    lineNo = 0
    while line:
        for word in line.split():
            lowerCaseWord = word.lower()
            if lowerCaseWord in wordsDict:
                wordsDict[lowerCaseWord]["total"] = (wordsDict[lowerCaseWord]["total"] + 1)
                wordsDict[lowerCaseWord]["lines"].append((shortName, lineNo))
            else:
                wordsDict[lowerCaseWord] = {"total" : 1, "lines" : [(shortName,lineNo)]}
        lineNo += 1
        line = inputFile.readline()

    print("num of Harry after reading from " + filename + " is " + str(wordsDict["harry"]["total"]))

    nowHarry = wordsDict["harry"]["total"]
    print("added " + str(nowHarry - prevHarry))
    prevHarry = nowHarry

print(str(wordsDict["expelliarmus"]))
