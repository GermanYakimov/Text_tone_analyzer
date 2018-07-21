# Copyright © 2017-2018. All rights reserved.
# Authors: German Yakimov, Aleksey Sheboltasov
# License: https://github.com/GermanYakimov/Text_tone_analyzer/blob/master/LICENSE
# Contacts: german@yakimov.su, alekseysheboltasov@gmail.com


class DocumentPreparer:
    def __init__(self):
        pass

    @staticmethod
    def split_into_unigrams(text):
        return text.split()

    @staticmethod
    def split_into_bigrams(text):
        unigrams = text.split()
        bigrams = list()

        if len(unigrams) >= 2:
            for unigram_index in range(len(unigrams) - 1):
                bigrams.append(unigrams[unigram_index] + ' ' + unigrams[unigram_index + 1])
        else:
            return None

        return bigrams

    @staticmethod
    def split_into_trigrams(text):
        unigrams = text.split()
        trigrams = list()

        if len(unigrams) >= 3:
            for unigram_index in range(len(unigrams) - 2):
                trigrams.append(unigrams[unigram_index] + ' ' + unigrams[unigram_index + 1] + ' ' + \
                                     unigrams[unigram_index + 2])
        else:
            return None

        return trigrams