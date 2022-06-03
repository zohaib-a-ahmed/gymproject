import pandas as pd
import http.client
from fuzzywuzzy import fuzz

#conn = http.client.HTTPSConnection("exercisedb.p.rapidapi.com")
#headers = {
 #   'X-RapidAPI-Host': "exercisedb.p.rapidapi.com",
 #   'X-RapidAPI-Key': "62e9927b85mshdb1756f38fb90fap17690djsna4da928a3d2d"
#    }
#conn.request("GET", "/exercises", headers=headers)
#res = conn.getresponse()
#data = res.read()

#exercisedf = pd.DataFrame(eval(data)) # how to make exercises into data frame

#upperlegsdf = exercisedf.loc[exercisedf['bodyPart'] == 'upper legs'] # how to sort exercises 

#targets = list(exercisedf['target'].drop_duplicates()) # create running LIST of targets

Str1 = "incline press"
Str2 = "dumbbell incline bench press"
Ratio = fuzz.ratio(Str1,Str2)
Ratio2 = fuzz.partial_ratio(Str1, Str2)
print(Ratio)
print(Ratio2)
