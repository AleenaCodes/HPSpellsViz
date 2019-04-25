import json

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

listOfSpells = {
  "accio" : {
    "description" : "brings an object to you",
    "type" : "charm" ,
  },
  "aguamenti" : {
    "description" : "creates a gush of water from the tip of the spell caster's wand",
    "type" : "conjuration"
  },
  "alohomora" : {
    "description" : "opens locks" ,
    "type" : "charm"
  },
  "anapneo" : {
    "description" : "clears the target's airways",
    "type": "healing spell"
  },
  "aparecium" : {
    "description" : "makes invisible ink become visible" ,
    "type" : "charm"
  },
  "avada kedavra" : {
    "description" : "kills your opponent",
    "type" : "unforgivable curse"
  },
  "avis" : {
    "description" : "makes birds fly out of the end of your wand",
    "type" : "conjuration"
  },
  "cave inimicum" : {
    "description" : "strengthens an enclosure from enemies",
    "type" : "spell"
  },
  "colloportus" : {
    "description" : "closes a door and binds it so that it can't be opened",
    "type" : "charm"
  },
  "confringo" : {
    "description" : "causes the item targeted to explode",
    "type" : "curse"
  },
  "confundus" : {
    "description" : "confounds your target, or makes them temporarily confused",
    "type" : "charm"
  },
  "conjunctivitis" : {
    "description" : "damages the eyesight of your opponent, making them seem to have pink eye",
    "type" : "curse"
  },
  "crucio" : {
    "description" : "tortures your opponent mercilessly" ,
    "type" : "unforgivable curse"
  },
  "defodio" : {
    "description" : "carves through material",
    "type" : "charm"
  },
  "deletrius" : {
    "description" : "erases the last spell cast by a wand so that it can't be discovered",
    "type" : "counter-spell"
  },
  "densaugeo" : {
    "description" : "makes teeth grow out of control",
    "type" : "hex"
  },
  "deprimo" : {
    "description" : "blasts holes in ground",
    "type" : "charm"
  },
  "diffindo" : {
    "description" : "makes seams split open, severs an object into two pieces",
    "type" : "charm"
  },
  "dissendium" : {
    "description" : "opens a specific passageway into a cellar",
    "type": "charm"
  },
  "duro" : {
    "description" : "turns an item to stone",
    "type" : "charm"
  },
  "engorgio" : {
    "description" : "makes an item larger, as in swollen",
    "type" : "charm"
  },
  "episkey" : {
    "description" : "heals relatively minor wounds",
    "type" : "healing spell"
  },
  "erecto" : {
    "description" : "erects a structure",
    "type" : "charm"
  },
  "expecto patronum" : {
    "description" : "creates a Patronus",
    "type" : "charm"
  },
  "expelliarmus" : {
    "description" : "disarms the target of the spell" ,
    "type" : "charm"
  },
  "expulso" : {
    "description" : "blows things up" ,
    "type" : "curse"
  },
  "ferula" : {
    "description" : "binds a broken limb with a splint and bandages",
    "type" : "healing spell"
  },
  "fidelius" : {
    "description" : "allows a secret to be hidden within the secret keeper's soul",
    "type" : "charm"
  },
  "finite incantatem" : {
    "description" : "stops any spell",
    "type" : "counter-spell"
  },
  "flagrate" : {
    "description" : "allows the user to write or draw in the air with fire",
    "type" : "charm"
  },
  "furnunculus" : {
    "description" : "causes a person to break out in boils",
    "type" : "jinx"
  },
  "geminio" : {
    "description" : "creates a duplicate of an item",
    "type" : "conjuration"
  },
  "glisseo" : {
    "description" : "turns stairs into a slide",
    "type" : "charm"
  },
  "homenum revelio" : {
    "description" : "reveals the presence of other humans",
    "type" : "charm"
  },
  "homorphus" : {
    "description" : "makes a werewolf or person disguised as an animal resume their human shape",
    "type" : "charm"
  },
  "impedimenta" : {
    "description" : "puts up an impediment that slows down something or someone that is coming toward you",
    "type" : "jinx"
  },
  "imperio" : {
    "description" : "allows the user to assume complete control of another person",
    "type" : "unforgivable curse"
  },
  "impervius" : {
    "description" : "repels water from a surface",
    "type" : "charm"
  },
  "incarcerous" : {
    "description" : "conjures up ropes",
    "type" : "conjuration"
  },
  "incendio" : {
    "description" : "lights a fire",
    "type" : "conjuration"
  },
  "langlock" : {
    "description" : "sticks tongue to roof of the mouth" ,
    "type" : "jinx"
  },
  "legilimens" : {
    "description" : "allows the user to gain access to another's mind and memories" ,
    "type" : "charm"
  },
  "levicorpus" : {
    "description" : "turns your opponent upside down and dangles them in thin air" ,
    "type" : "jinx"
  },
  "liberacorpus" : {
    "description" : "frees a body that has been caught up by the levicorpus spell",
    "type" : "counter-spell"
  },
  "locomotor" : {
    "description" : "levitates a target off the ground",
    "type" : "charm"
  },
  "locomotor mortis" : {
    "description" : "locks an opponent's legs together",
    "type" : "curse"
  },
  "lumos" : {
    "description" : "creates light",
    "type" : "charm"
  },
  "meteolojinx recanto" : {
    "description" : "causes weather effects caused by incantations to cease",
    "type" : "counter-spell"
  },
  "mobiliarbus" : {
    "description" : "used to move a tree from one place to another",
    "type" : "charm"
  },
  "mobilicorpus" : {
    "description" : "used to move a body from one place to another",
    "type" : "charm"
  },
  "morsmordre" : {
    "description" : "used to summon the Dark Mark",
    "type" : "curse"
  },
  "muffliato" : {
    "description" : "causes a buzzing noise to surround a limited area",
    "type" : "charm"
  },
  "nox" : {
    "description" : "extinguishes light",
    "type" : "counter-spell"
  },
  "obliviate" : {
    "description" : "erases a person's memories of an event",
    "type" : "charm"
  },
  "obscuro" : {
    "description" : "blindfolds target",
    "type" : "conjuration"
  },
  "oppugno" : {
    "description" : "assaults target with directed object(s)",
    "type" : "jinx"
  },
  "orchideous" : {
    "description" : "conjures a bunch of flowers from the user's wand",
    "type" : "conjuration"
  },
  "petrificus totalus" : {
    "description" : "petrifies an opponent totally",
    "type" : "curse"
  },
  "piertotum locomotor" : {
    "description" : "animates target",
    "type" : "charm"
  },
  "point me" : {
    "description" : "makes the user's wand act like a compass",
    "type" : "charm"
  },
  "portus" : {
    "description" : "turns any item into a portkey",
    "type" : "charm"
  },
  "prior incantato" : {
    "description" : "reveals to you the last spell that a wand was used to cast",
    "type" : "charm"
  },
  "protego" : {
    "description" : "protects the user, and sends a spell back on an opponent" ,
    "type" : "charm"
  },
  "protego horribillis" : {
    "description" : "protects against darkest magic" ,
    "type" : "charm"
  },
  "protego totalum" : {
    "description" : "shields an area" ,
    "type" : "charm"
  },
  "quietus" : {
    "description" : "makes things quiet",
    "type" : "charm"
  },
  "reducio" : {
    "description" : "shrinks an item",
    "type" : "charm"
  },
  "reducto" : {
    "description" : "blasts solid objects into pieces",
    "type" : "curse"
  },
  "relashio" : {
    "description" : "releases something from being constrained or held",
    "type" : "jinx"
  },
  "rennervate" : {
    "description" : "used to wake up a stunned person",
    "type" : "charm"
  },
  "reparo" : {
    "description" : "repairs broken items",
    "type" : "charm"
  },
  "repello muggletum" : {
    "description" : "makes an area invisible to muggles",
    "type" : "charm"
  },
  "revelio" : {
    "description" : "causes something that is hidden to be revealed",
    "type" : "charm"
  },
  "rictusempra" : {
    "description" : "causes a person to curl up in laughter, as if being tickled",
    "type" : "charm"
  },
  "riddikulus" : {
    "description" : "makes a boggart assume a “ridiculous” form",
    "type" : "charm"
  },
  "salvio hexia" : {
    "description" : "deflects any hexes cast toward a specific location",
    "type" : "charm"
  },
  "scourgify" : {
    "description" : "used to clean dirt or other material off of a surface",
    "type" : "charm"
  },
  "sectumsempra" : {
    "description" : "causes lacerations to appear all over an opponent's body",
    "type" : "curse"
  },
  "serpensortia" : {
    "description" : "conjures a snake",
    "type" : "conjuration"
  },
  "silencio" : {
    "description" : "makes the target of the spell unable to make any sound",
    "type" : "charm"
  },
  "sonorus" : {
    "description" : "amplifies the user's voice",
    "type" : "charm"
  },
  "specialis revelio" : {
    "description" : "reveals spells cast on objects or potions",
    "type" : "charm"
  },
  "stupefy" : {
    "description" : "knocks an opponent insensible temporarily",
    "type" : "charm"
  },
  "tarantallegra" : {
    "description" : "forces an opponent's legs to dance uncontrollably",
    "type" : "jinx"
  },
  "tergeo" : {
    "description" : "scours something clean",
    "type" : "charm"
  },
  "waddiwasi" : {
    "description" : "removes a stuck object",
    "type" : "jinx"
  },
  "wingardium leviosa" : {
    "description" : "allows the user to make an object levitate",
    "type" : "charm"
  },
}

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

# print(str(wordsDict["expelliarmus"]))
# print(str(wordsDict["incantato"]))
# print(str(wordsDict["revelio"]))
# print(str(wordsDict["scourgify"]))
# print(str(wordsDict["inimicum"]))
# print(str(wordsDict["kedavra"]))

for fullSpellName in listOfSpells:
    splitSpellName = fullSpellName.split()
    spellName = ""

    if len(splitSpellName) > 1:
        spellName = splitSpellName[1]
    else:
        spellName = splitSpellName[0]

    if splitSpellName[0] == "homenum":
        spellName = "homenum"
    if splitSpellName[0] == "specialis":
        spellName = "specialis"
    if splitSpellName[0] == "piertotum":
        spellName = "piertotum"

    # print("looking at spell" + spellName)

    if spellName in wordsDict:
        listOfSpells[fullSpellName]["total"] = wordsDict[spellName]["total"]
        listOfSpells[fullSpellName]["lines"] = wordsDict[spellName]["lines"]
    else:
        print(spellName + " is not in wordsDict")

print(str(wordsDict["revelio"]))
print(str(listOfSpells["revelio"]))

with open('outputData.json', 'w') as outfile:
    json.dump(listOfSpells, outfile)

print("finished")
