""" Script creates JSON DICTs
    Only needs to be run ONCE per container instance IF needed """

import json
import csv
import os

BASE_PATH =     os.path.dirname(__file__)
CMU_CSV =       os.path.join(BASE_PATH, "cmudict.csv")
CMU_JSON =      os.path.join(BASE_PATH, "cmu_dict.json")
ARPABET_CSV =   os.path.join(BASE_PATH, "arpabet.csv")
ARPABET_JSON =  os.path.join(BASE_PATH, "arpabet_dict.json")       #absolute file paths

cmu_dict = {}       #DICT[WORD] = PHONEMES
arpabet_dict = {}   #DICT[ARPABET] = IPA

with open(CMU_CSV, "r") as file:              #read csv into DICT
    for i in range(126):
        next(file)                                  #skip uneeded/metadata

    for line in file:
        line = line.strip()
        word, phonemes = line.split(maxsplit=1)
        cmu_dict[word.lower()] = phonemes

with open(CMU_JSON, "w") as json_file:           #convert DICT to JSON for future use
    json.dump(cmu_dict, json_file, indent=5)

with open(ARPABET_CSV, "r") as file:
    next(file)                            #skip column names
    reader = csv.reader(file)

    for row in reader:
        arpabet_dict[row[0]] = row[1]

with open(ARPABET_JSON, "w") as json_file:
    json.dump(arpabet_dict, json_file, indent=5)
