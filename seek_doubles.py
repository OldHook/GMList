import os
from operator import itemgetter
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

dirName = 'c:\Work\Python\Projects\Other\GMList\Source'
aData = []
names = os.listdir(dirName)
for name in names:
    fullname = os.path.join(dirName, name)
    if os.path.isfile(fullname):
        with open(fullname, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            line = lines[1]
            line = line.replace('&#39;','\'')
            line = line.replace('\'\'','\'')
            line = line.replace('&amp;','&')
            if line[0:9] != '"","","",':
                #print(line[1:-2])
                data = line[1:-2].split('","')
                title = data[0]
                album = data[1]
                performer = data[2]
                length = data[3]
                score = data[4]
                deleted = data[6]
                if len(deleted) == 0:
                    aData.append([performer, album, title, score, deleted, length])
aData.sort(key=itemgetter(0,1,2))
#with open('c:\Work\Python\Projects\Other\GMList\list.txt', 'w', encoding="utf-8") as f:
#    f.write('\"Performer\","Album\","Title\","Score\","Deleted\"\n')
#    for item in aData:
#        f.write('\"'+item[0]+'\","'+item[1]+'\","'+item[2]+'\","'+item[3]+'\","'+item[4]+'\"\n')

#Поиск дублей
i = 0
while i < len(aData)-1:
    j = i + 1
    while j < len(aData)-1:
        if i != j:
            if similar(aData[i][2], aData[j][2]) > 0.8:
                len1 = float(aData[i][5]) - float(aData[i][5]) * 0.05
                len2 = float(aData[i][5]) + float(aData[i][5]) * 0.05
                len3 = float(aData[j][5])
                if len1 <= len3 <= len2:
                    print(i, aData[i][2]+':'+aData[i][5], j, aData[j][2]+':'+aData[j][5])
        j += 1
    i += 1
