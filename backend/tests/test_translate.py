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

def test_translate_sentence_with_special_characters():
    assert translate_sentence("why can't i have cake? I really, really love cake!") == "/waɪ kænt aɪ hæv keɪk aɪ ɹɪli ɹɪli lʌv keɪk/"
    assert translate_sentence("YES, I SURE DO LOVE CAKE WITH A TALL GLASS OF MILK.") == "/jɛs aɪ ʃʊɹ du lʌv keɪk wɪð ʌ tɔl glæs ʌv mɪlk/"

def test_translate_sentence_without_special_characters():
    assert translate_sentence("I AM HERE LIVING MY BEST LIFE") == "/aɪ æm hiɹ lɪvɪŋ maɪ bɛst laɪf/"
    assert translate_sentence("i am here living my best life") == "/aɪ æm hiɹ lɪvɪŋ maɪ bɛst laɪf/"

    assert translate_sentence("BECAUSE SCHOOL IS STARTING I WILL SPEND LESS TIME RELAXING") == "/bɪkɔz skul ɪz stɑɹtɪŋ aɪ wɪl spɛnd lɛs taɪm ɹɪlæksɪŋ/"
    assert translate_sentence("because school is starting i will spend less time relaxing") == "/bɪkɔz skul ɪz stɑɹtɪŋ aɪ wɪl spɛnd lɛs taɪm ɹɪlæksɪŋ/"
