from time import time
import json
import datetime
import requests


def requestData(AnimeName, link):
    url = f"https://api.jikan.moe/v3/search/anime?q={AnimeName}&limit=16"
    data = json.loads(requests.get(url).text)
    return {"synopsis": data['results'][0]['synopsis'], "image_url": data['results'][0]['image_url'], "link": link}


def getTimeDif():
    with open('\\Web-Anime\\data.json', 'r') as fp:
        date = datetime.datetime.now()
        DateFile = json.load(fp)
        DateFile = datetime.datetime(DateFile["date"][0], DateFile["date"][1],
                                     DateFile["date"][2], DateFile["date"][3], DateFile["date"][4], DateFile["date"][5])
        dif = date - DateFile
        dif = divmod(dif.seconds, 60)
        return True


with open('\\python\\Web-Anime\\data.json', 'r+') as fp:
    date = datetime.datetime.now()
    DateFile = json.load(fp)
    DateFile = datetime.datetime(DateFile["date"][0], DateFile["date"][1],
                                 DateFile["date"][2], DateFile["date"][3], DateFile["date"][4], DateFile["date"][5])
    dif = date - DateFile
    dif = divmod(dif.seconds, 60)
    print(dif[0])

    if dif[0] >= 0:
        with open("\\python\\Web-Anime\\result.json", "r") as fp1:
            data = json.load(fp1)
            NewDico = {'date': (date.year, date.month, date.day,
                                date.hour, date.minute, date.second)}
            TmpDico = {}
            i = 0
            tpTmp = time()
            lenData = len(data.keys())
            print(lenData)
            for k, v in data.items():
                i += 1
                TmpDico[k] = requestData(k, v)
                print(
                    f"i : {i} || time : {str(datetime.timedelta(seconds=((time() - tpTmp)/i)*lenData))}")

        NewDico["Anime"] = TmpDico
        json.dump(NewDico, fp)
