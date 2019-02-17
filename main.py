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


prizes = json.load(open('prize.json', 'r'))
laureate = json.load(open('laureate.json', 'r'))
country = json.load(open('country.json', 'r'))

datasets = { **prizes, **laureate}

#def getByYear(year, category):










