""" Script creates JSON DICTs
    Only needs to be run ONCE per container instance IF needed """

import json
import csv

cmu_dict = {}       #DICT[WORD] = PHONEMES
arpabet_dict = {}   #DICT[ARPABET] = IPA

with open("cmudict.csv", "r") as file:              #read csv into DICT
    for i in range(126):
        next(file)                                  #skip uneeded/metadata

    for line in file:
        line = line.strip()
        word, phonemes = line.split(maxsplit=1)
        cmu_dict[word.lower()] = phonemes

with open("cmu_dict.json", "w") as json_file:           #convert DICT to JSON for future use
    json.dump(cmu_dict, json_file, indent=5)

with open("arpabet.csv", "r") as file:
    next(file)                            #skip column names
    reader = csv.reader(file)

    for row in reader:
        arpabet_dict[row[0]] = row[1]

with open("arpabet_dict.json", "w") as json_file:
    json.dump(arpabet_dict, json_file, indent=5)
