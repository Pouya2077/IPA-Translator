import os
import json

BASE_PATH =         os.path.dirname(__file__)
CMU_DICT_PATH =     os.path.join(BASE_PATH, "../phase1/cmu_dict.json")
ARPABET_DICT_PATH = os.path.join(BASE_PATH, "../phase1/arpabet_dict.json")

with open(CMU_DICT_PATH) as file:
    CMU_DICT = json.load(file)

with open(ARPABET_DICT_PATH) as file:
    ARPABET_DICT = json.load(file)      #setting up dicts for tests to use

