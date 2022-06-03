import http.client
import pandas as pd
from fuzzywuzzy import fuzz

# Retrieve data
conn = http.client.HTTPSConnection("exercisedb.p.rapidapi.com")
headers = {
    'X-RapidAPI-Host': "exercisedb.p.rapidapi.com",
     'X-RapidAPI-Key': "62e9927b85mshdb1756f38fb90fap17690djsna4da928a3d2d"
}
conn.request("GET", "/exercises", headers=headers)
res = conn.getresponse()
data = res.read()

# Create reference variables
exercisedf = pd.DataFrame(eval(data))
targets = list(exercisedf['target'].drop_duplicates())
bodyparts = list(exercisedf['bodyPart'].drop_duplicates())

def getMovementsForArea(something:str) -> list:
        # Check if inputted target area is in bodyparts or targets and return associated movements as a list

        if something in targets:
            return list(exercisedf.loc[exercisedf['target'] == something]['name']) # return associated exercises
        else:
            if something in bodyparts:
                return list(exercisedf.loc[exercisedf['bodyPart'] == something]['name']) # return associated exercises
            else:
                raise ValueError("Target bodypart not found.")

def getSimilarMovements(someExercise:str) -> list:
    # Search exercises for names similar to key input
    similarNames = []

    # Gather similar exercises
    exercises = list(exercisedf['name'])
    for exercise in exercises:
        if(fuzz.ratio(exercise, someExercise) > 60):
            similarNames.append(exercise)
        else:
            if(fuzz.partial_ratio(exercise, someExercise) > 70):
                similarNames.append(exercise)
    
    # basic selection sort to bring most similar to from of the list
    for i in range(len(similarNames)):
        min_idx = i
        for j in range(i+1, len(similarNames)):
            if fuzz.ratio(similarNames[min_idx], someExercise) < fuzz.ratio(similarNames[j], someExercise):
                min_idx = j     
        similarNames[i], similarNames[min_idx] = similarNames[min_idx], similarNames[i]

    return similarNames



