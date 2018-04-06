#!/usr/bin/python3
import urllib.request
import os
import json
Wea_url = "https://free-api.heweather.com/s6/weather/now?location=CN101070201&key=e5a835b982ba40d9a897b42b5b8c883f"
Lif_url = "https://free-api.heweather.com/s6/weather/lifestyle?location=CN101070201&key=e5a835b982ba40d9a897b42b5b8c883f"
Air_url = "https://free-api.heweather.com/s6/air/now?location=CN101070201&key=e5a835b982ba40d9a897b42b5b8c883f"
def getWeather(url):
    data = urllib.request.urlopen(url).read()
    txt = data.decode(encoding="utf-8",errors="strict")
    index = 0
    a =0
    while(index != -1):
        index = txt.find("txt",index+1,len(txt))
        a += 1
        if(index > 1):
            txt = txt[:index+2] + str(a) + txt[index+3:]
    return txt
#    dejson = json.loads(txt)
#    print(dejson)

def write_txt():
    txt = getWeather(Wea_url)
    txt = txt +'\n' + getWeather(Lif_url) + '\n'
    f = open("/home/pi/Graduation-Project/untitled/qrc/data.json","w")
    f.write(txt)
    f.close()

def deal_data(json):
    if(isinstance(json,dict)):
        for i in list(json.keys()):
            if(isinstance(json[i],list)):
                for i in json[i]:
                    deal_data(i)
            else:
                print("Head:   ",i)
                deal_data(json[i])
    else:
        print("Center: ",json)

if __name__ == '__main__':
    write_txt()
