""" Functionality to translate words to IPA """

import json

with open("dict.json") as file:
    DICT = json.load(file)          #CMUdict available locally

def convert_to_ipa(char):
    """ Covert from ARPAbet to IPA """

    return char

def convert_phonemes(phonemes):
    """ Convert phonemes to IPA word """
    chars = list(phonemes)
    ipa_word = ""

    for char in chars:
        ipa_word += convert_to_ipa(char)

    return ipa_word

def translate_word(word):
    """ Convert English word to IPA """

    phonemes = DICT[word.lower()]
    return convert_phonemes(phonemes)

#TODO frontend checks if word provided is English (latin alphabet)
#if word cannot be translated, activate phase2

print(convert_phonemes("word"))