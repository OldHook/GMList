import os
from operator import itemgetter

dirName = os.path.normpath(os.path.join(os.getcwd(), 'Source'))
destinationFileName = os.path.normpath(os.path.join(os.getcwd(), 'list.txt'))
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
                score = data[4]
                deleted = data[6]
                if len(deleted) == 0:
                    aData.append([performer, album, title, score, deleted])

aData.sort(key=itemgetter(0,1,2))

with open(destinationFileName, 'w', encoding="utf-8") as f:
    f.write('\"Performer\","Album\","Title\","Score\","Deleted\"\n')
    for item in aData:
        f.write('\"'+item[0]+'\","'+item[1]+'\","'+item[2]+'\","'+item[3]+'\","'+item[4]+'\"\n')
