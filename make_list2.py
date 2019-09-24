import os
from operator import itemgetter

destinationFileName = os.path.normpath(os.path.join(os.getcwd(), 'list.txt'))
aData = []
aFavorites = []

dirName = os.path.normpath(os.path.join(os.getcwd(), 'Tracks'))
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
                data = line[1:-2].split('","')
                title = data[0]
                album = data[1]
                performer = data[2]
                timeMSec = data[3]
                score = data[4]
                deleted = data[6]

                seconds = round(int(timeMSec) / 1000);
                minutes = seconds // 60;
                seconds = seconds % 60;
                sLength = str(minutes) + ':' + '{:02d}'.format(seconds);
                aData.append([performer, album, title, score, sLength, deleted, ""]);

dirName = os.path.normpath(os.path.join(os.getcwd(), 'Favorites'))
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
                data = line[1:-2].split('","')
                title = data[0]
                album = data[1]
                performer = data[2]
                timeMSec = data[3]
                score = data[4]
                deleted = data[6]

                seconds = round(int(timeMSec) / 1000);
                minutes = seconds // 60;
                seconds = seconds % 60;
                sLength = str(minutes) + ':' + '{:02d}'.format(seconds);
                aFavorites.append([performer, album, title, score, sLength, deleted, "Да"])

for i in range(len(aFavorites)):
    FavSong = aFavorites[i];
    found = False;
    for j in range(len(aData)):
        Song = aData[j];
        if FavSong[2] == Song[2] and FavSong[0] == Song[0] and FavSong[1] == Song[1] and FavSong[4] == Song[4]:
            found = True;
            break;
    if found:
        aData[j][6] = "Да";
    else:
        aData.append(FavSong);

aData.sort(key=itemgetter(0,1,2))

with open(destinationFileName, 'w', encoding="utf-8") as f:
    f.write('\"Performer\","Album\","Title\","Score\","Length\","Deleted\","Favorite\"\n')
    for item in aData:
        f.write('\"'+item[0]+'\","'+item[1]+'\","'+item[2]+'\","'+item[3]+'\","'+item[4]+'\","'+item[5]+'\","'+item[6]+'\"\n')
