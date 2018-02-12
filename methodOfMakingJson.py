# coding: utf-8
import pandas as pd
import time
import json

place = "XXXXXXXXXDirectory of your python fileXXXXXXXXX"

######################
# Prepared data
######################
f = open(place + 'tpl.txt')
listOut = []

for line in f:
    trimmed = line.rstrip('\r')
    trimmed = line.rstrip('\n')

    listIn = []
    listIn = trimmed.split(",")
    listOut.append(listIn)

f.close()

######################
# pandas
######################
time.sleep(5)
startPd = time.time()

df = pd.DataFrame(listOut)
df.columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
pandasJson = df.to_json(orient="records")
# print(pandasJson)

elapsedTimePd = time.time() - startPd
print ("elapsedTimePd:{0}".format(elapsedTimePd) + "[sec]")

# file output
#file = open('pandas.json', 'w')
# file.write(pandasJson)
# file.close()


######################
# for
######################
time.sleep(5)
startFor = time.time()

columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
listTemp = []

for listOutEach in listOut:
    dictTemp = {}

    for column in range(len(listOutEach)):
        dictTemp.update({columns[column]: listOutEach[column]})

    listTemp.append(dictTemp)

forJson = json.dumps(listTemp)
# print(forJson)

elapsedTimeFor = time.time() - startFor
print ("elapsedTimeFor:{0}".format(elapsedTimeFor) + "[sec]")
