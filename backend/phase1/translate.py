""" Functionality to translate words to IPA """

import json
import re
import os

BASE_PATH = os.path.dirname(__file__)
CMU_DICT_PATH = os.path.join(BASE_PATH, "cmu_dict.json")
ARPABET_DICT_PATH = os.path.join(BASE_PATH, "arpabet_dict.json")

with open(CMU_DICT_PATH) as file:
    CMU_DICT = json.load(file)          #make dicts available locally

with open(ARPABET_DICT_PATH) as file:
    ARPABET_DICT = json.load(file)

def remove_specials(chars):
    """ Remove special characters from chars """
    phonemes = []

    for char in chars:
        char = re.sub(r'\d', '', char)      #0-9 removal (stress)
        char = re.sub(r'\W', '', char)      #special character removal
        phonemes.append(char)

    return phonemes

def convert_to_ipa(arpabet_char):
    """ Covert from ARPAbet to IPA """
    return ARPABET_DICT[arpabet_char.upper()]

def convert_phonemes(phonemes):
    """ Convert phonemes to IPA word """
    chars = phonemes.split(" ")
    chars = remove_specials(chars)
    ipa_word = ""

    for char in chars:
        ipa_word += convert_to_ipa(char)

    return ipa_word

def translate_word(word):
    """ Convert English word to IPA """

    word = re.sub(r'[?!]', '', word)        #explicity removal irrelevant punctuation
    phonemes = CMU_DICT[word.lower()]
    return convert_phonemes(phonemes)

def translate_sentence(sentence):
    """ Convert sentence (entry beyond one word) into IPA """

    ipa_sentence = ""
    words = sentence.split(" ")
    for word in words:
        ipa_sentence = ipa_sentence + " " + translate_word(word)

    return "/" + ipa_sentence.strip() + "/"

#TODO frontend checks if word provided is English (latin alphabet)
#TODO consider adding functionality to support punctuation
#TODO if word cannot be translated, activate phase2