import os
import json
import csv

BASE_PATH =         os.path.dirname(__file__)
CMU_DICT_PATH =     os.path.join(BASE_PATH, "../phase1/cmu_dict.json")
ARPABET_DICT_PATH = os.path.join(BASE_PATH, "../phase1/arpabet_dict.json")
ARPABET_CSV_PATH =  os.path.join(BASE_PATH, "../phase1/arpabet.csv")

with open(CMU_DICT_PATH) as file:
    CMU_DICT = json.load(file)

with open(ARPABET_DICT_PATH) as file:
    ARPABET_DICT = json.load(file)      #setting up dicts for tests to use

def test_arpabet_dict_correct_values():
    with open(ARPABET_CSV_PATH, "r") as file:
        next(file)
        reader = csv.reader(file)

        for row in reader:
            assert ARPABET_DICT[row[0]] == row[1]

# TODO come back for cmu_dict testing
