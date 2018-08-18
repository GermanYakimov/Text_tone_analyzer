# Copyright © 2018. All rights reserved.
# Author: German Yakimov

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from Python.Services.Logger import Logger

# logic in splitting into bigrams and trigrams (word order sorting)


class DocumentPreparer:
    def __init__(self):
        self.__logger = Logger()

        if not self.__logger.configured:
            self.__logger.configure()

        self.__logger.info('DocumentPreparer was successfully initialized.', 'DocumentPreparer.__init__()')

    @staticmethod
    def split_into_unigrams(text):
        return text.split()

    @staticmethod
    def split_into_bigrams(text):
        unigrams = text.split()
        bigrams = list()

        if len(unigrams) >= 2:
            for unigram_index in range(len(unigrams) - 1):
                bigram = ' '.join(sorted([unigrams[unigram_index], unigrams[unigram_index + 1]])).strip()
                bigrams.append(bigram)

            return bigrams

    @staticmethod
    def split_into_trigrams(text):
        unigrams = text.split()
        trigrams = list()

        if len(unigrams) >= 3:
            for unigram_index in range(len(unigrams) - 2):
                trigram = ' '.join(sorted(
                    [unigrams[unigram_index],
                     unigrams[unigram_index + 1],
                     unigrams[unigram_index + 2]])).strip()

                trigrams.append(trigram)

            return trigrams
