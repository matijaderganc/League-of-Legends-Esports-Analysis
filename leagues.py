import csv
import os
import requests 
import re
from bs4 import BeautifulSoup

linki = []
linki = []
lige_format = [("LEC", 2019, 2025, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs'], 'LEC'),
               ("EU_LCS", 2014, 2019, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs'], 'LEC'),
               ("NA_LCS", 2014, 2019, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs'], 'LCS'),
               ("LCS", 2019, 2021, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs'], 'LCS'),
               ("LCS", 2021, 2022, ['Spring_Season', 'Lock_In', 'Mid-Season_Showdown', 'Summer_Season', 'Championship'], 'LCS'),
               ("LCS", 2022, 2025, ['Spring_Season', 'Lock_In', 'Spring_Playoffs', 'Summer_Season', 'Championship'], 'LCS'),
               ("LCK", 2013, 2025, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs', 'Regional_Finals'], 'LCK'),
               ("LPL", 2014, 2025, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs', 'Regional_Finals'], 'LPL'),
               ]
#ime lige, začetek, konec, deli sezone v ligi

#občasno se izvajajo tudi turnirji, ki so v drugačni obliki kot lige
turnirji_format = [("_Season_World_Championship", 2014, 2017, 'International'), 
                   ("_Season_World_Championship/Main_Event", 2017, 2024, 'International'),
                   ("_Mid-Season_Invitational", 2015, 2017, 'International'),
                    ("_Mid-Season_Invitational/Main_Event", 2017, 2020, 'International'),
                   ("_Mid-Season_Invitational", 2021, 2024, 'International')
]

linki_lige = []

for liga in lige_format:
    for leto in range(liga[1], liga[2]):
        for del_sezone in liga[3]:
            linki.append(f'https://lol.fandom.com/wiki/{liga[0]}/{leto}_Season/{del_sezone}/Match_History')
            linki_lige.append(liga[4])


for turnir in turnirji_format:
    for leto in range(turnir[1], turnir[2]):
        linki.append(f'https://lol.fandom.com/wiki/{leto}{turnir[0]}/Match_History')
        linki_lige.append(turnir[3])


