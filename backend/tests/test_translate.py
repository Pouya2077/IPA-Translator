from phase1 import translate_word
from phase1 import translate_sentence

def test_translate_word_with_special_characters():
    assert translate_word("DOESN'T") == "dʌzʌnt"
    assert translate_word("doesn't") == "dʌzʌnt"

    assert translate_word("CAN'T?") == "kænt"
    assert translate_word("can't?") == "kænt"

def test_short_length_word_translation():
    assert translate_word("ME") == "mi"
    assert translate_word("me") == "mi"

def test_medium_length_word_translation():
    assert translate_word("MOTHER") == "mʌðər"
    assert translate_word("mother") == "mʌðər"

def test_long_length_word_translation():
    assert translate_word("FANTASTICALLY") == "fæntæstɪkli"
    assert translate_word("fantastically") == "fæntæstɪkli"


