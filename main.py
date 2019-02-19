"""
    Data structures of 2 jayson data sets:
        prizes:
                - year
                - category:
                            - physics
                            - economics
                            - medicine
                            - chemistry
                            - literature
                            - peace
                - overall motivation (optionally)
                - laureates [...] (the same as laureates data set but additional
                                    one attribute is |share|: which means how many
                                    people share the Nobel Prize in certain category)
        laureates:
                    - id
                    - first name
                    - surname
                    - born(date)
                    - died(date)
                    - bornCountry
                    - bornCountryCode
                    - diedCity
                    - gender
                    - prizes []
Nobel Prizes can be displayed by certain:
                                            - year/ years and certain category
                                            - laureate
------------------------------------------------------------------------------------------------------------------------
    Note in Python we can pack and unpack argument parameters with * for tuple list, or ** for dictionary
"""
import json

dataset = {**json.load(open('prize.json', 'r')), **json.load(open('laureate.json', 'r'))}

def printCategories(data):
    categories = []

    for item in data:
        if item['category'] not in categories:
            categories.append(item['category'])

    print("Chose category from the following:%s"%'\n\t - '.join(categories))

print("Nobel Prize Finder finds for you information about nobel prizes :)\n\n\n"
      "Type in correct order prize category and year that u interested in\n"
      "Tip: press 'Enter' after each parameter you type\n\n")
printCategories(dataset['prizes'])
category = input("Enter category name: ")
year = input("Chose year from 1901 till today: ")










