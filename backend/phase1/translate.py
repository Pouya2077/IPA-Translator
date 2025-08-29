""" Functionality to translate words to IPA """

import json

with open("cmu_dict.json") as file:
    CMU_DICT = json.load(file)          #CMUdict available locally

with open("arpabet_dict.json") as file:
    ARPABET_DICT = json.load(file)

def convert_to_ipa(arpabet_char):
    """ Covert from ARPAbet to IPA """
    return ARPABET_DICT[arpabet_char]

def convert_phonemes(phonemes):
    """ Convert phonemes to IPA word """
    chars = list(phonemes)
    ipa_word = ""

    for char in chars:
        ipa_word += convert_to_ipa(char)

    return ipa_word

def translate_word(word):
    """ Convert English word to IPA """

    phonemes = CMU_DICT[word.lower()]
    return convert_phonemes(phonemes)

#TODO frontend checks if word provided is English (latin alphabet)
#if word cannot be translated, activate phase2

print(convert_phonemes("word"))