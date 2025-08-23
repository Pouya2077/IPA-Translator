""" Module contains dictionary and its functions """

#DICT[WORD] = PHONEMES
DICT = {}

with open("cmudict.csv", "r") as file:
    for i in range(126):
        next(file)

    for line in file:
        line = line.strip()
        word, phonemes = line.split(maxsplit=1)
        DICT[word] = phonemes

# Can wrangle and make dict permanent data structure if needed 
