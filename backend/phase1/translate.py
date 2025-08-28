""" Functionality to translate words to IPA """

import json

with open("dict.json") as file:
    DICT = json.load(file)          #CMUdict available locally

def convert_phonemes(phonemes):
    """ Convert phonemes to IPA word """

    return phonemes

def translate_word(word):
    """ Take English word and convert to IPA """

    phonemes = DICT[word.lower()]
    return convert_phonemes(phonemes)

#TODO frontend checks if word provided is English
#if word cannot be translated, activate phase2
