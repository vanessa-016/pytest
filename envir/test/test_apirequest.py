import json

path='/Applications/Project/envir/test/gg.json'

with open(path) as content:
    loadJson = json.load(content)#Solo este cambio es

for i in loadJson ['heroes']['person']:
    print (i['heroName']) 


