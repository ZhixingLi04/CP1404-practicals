"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read the programming language details file, save as objects, and display them."""
    languages = []
    file = open('languages.csv', 'r')
    file.readline()
    for line in file:
        fields = line.strip().split(',')
        if len(fields) == 5:
            reflection = fields[2] == "Yes"
            pointer = fields[4] == "Yes"
            language = ProgrammingLanguage(fields[0], fields[1], reflection, int(fields[3]), pointer)
            languages.append(language)
        else:
            print(f"Error: Line split into unexpected number of fields: {fields}")
    file.close()

    for language in languages:
        print(language)


def use_csv():
    """Read the language file using the csv module."""
    file = open('languages.csv', 'r', newline='')
    file.readline()
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()


def use_namedtuple():
    """Read the language file using a named tuple."""
    file = open('languages.csv', 'r', newline='')
    file_field_names = file.readline().strip().split(',')
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer')
    reader = csv.reader(file)

    for row in reader:
        language = Language._make(row)
        print(language)
    file.close()


def use_csv_namedtuple():
    """Read the language file using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer')
    file = open("languages.csv", "r")
    file.readline()
    reader = csv.reader(file)
    for row in reader:
        language = Language(*row)
        print(language.name, 'was released in', language.year)
        print(language)

main()



