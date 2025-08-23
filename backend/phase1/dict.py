""" Module contains dictionary and its functions """

import csv

DICT = {} #dict[WORD] = PHONEMES 

with open("cmudict.csv", "r") as file:
    
