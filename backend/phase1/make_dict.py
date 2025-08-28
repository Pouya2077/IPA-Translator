""" Create JSON DICT
    Only needs to be run ONCE per container instance IF needed"""

import json

cmu_dict = {}   #DICT[WORD] = PHONEMES

with open("cmudict.csv", "r") as file:          #read csv into DICT
    for i in range(126):
        next(file)

    for line in file:
        line = line.strip()
        word, phonemes = line.split(maxsplit=1)
        cmu_dict[word.lower()] = phonemes         #converting to list here is intensive

with open("dict.json", "w") as json_file:       #convert DICT to JSON for future use
    json.dump(cmu_dict, json_file, indent=5)

