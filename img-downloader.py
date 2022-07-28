import csv
import requests
import os

def read_csv():
    with open("data.csv",'r',encoding="utf-8") as file:
        reader = csv.reader(file)
        line = 0
        data = []
        for row in reader:
            if line == 0:
                pass
            else:
                data.append({'name': row[0],'url': row[1]})
            line += 1
    return data

def downloadSaveImg ():
    data = read_csv()
    os.chdir(r"C:\Users\juand\OneDrive\Documentos\python\images")
    for x in data:
        res = requests.get(x["url"])
        name = x['name'].lower().replace(" ","_")
        file = open(f'{name}.jpg','wb')
        file.write(res.content)
        print(f"{name} is saved")
        file.close()

downloadSaveImg ()