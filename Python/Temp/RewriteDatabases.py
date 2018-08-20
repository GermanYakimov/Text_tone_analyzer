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

from Python.Services.PathService import PathService
from Python.Services.Lemmatizer.Lemmatizer import Lemmatizer
import sqlite3
import csv
from pprint import pprint

path_service = PathService()
lemmatizer = Lemmatizer()


def get_all_entries(database):
    path_to_db = path_service.get_path_to_database(database)

    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    request = "SELECT * FROM 'Data'"
    cursor.execute(request)

    return cursor.fetchall()


def optimize_data(data, save_info=True):
    if save_info:
        return [[entry[0], entry[1], entry[2]] for entry in data]
    else:
        return [entry[0] for entry in data]


def dump_to_csv(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in data:
            entry[1], entry[2] = str(entry[1]), str(entry[2])
            file.write(';'.join(entry) + '\n')


def read_dump(dump_name):
    data = list()
    with open(dump_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            entry = row[0].split(';')
            entry[1], entry[2] = int(entry[1]), int(entry[2])
            data.append(entry)

    return data


def lemmatize_dump(data):
    lemmatized_data = list()

    for n, entry in enumerate(optimize_data(data, save_info=False)):
        lemmatized_entry = lemmatizer.lead_to_initial_form(entry)

        if lemmatized_entry:
            lemmatized_data.append(lemmatized_entry)

        print(n)

    return lemmatized_data


def dump_lemmatized_data_to_new_dump(data, new_dump_name):
    with open(new_dump_name, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(entry + '\n')


data = read_dump('trigrams_dump.csv')

print(len(data))
data = lemmatize_dump(data)
print(len(data))

dump_lemmatized_data_to_new_dump(data, 'lemmatized_trigrams_dump.csv')
