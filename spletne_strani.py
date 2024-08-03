import csv
import os
import requests 
import re
from bs4 import BeautifulSoup

linki = []
lige_format = [("LEC", 2019, 2024, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("EU_LCS", 2014, 2019, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("NA_LCS", 2014, 2019, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("LCS", 2019, 2024, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("LCK", 2016, 2024, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs', 'Regional_Finals']),
               ("LPL", 2014, 2024, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs', 'Regional_Finals']),
               ]
#ime lige, začetek, konec, deli sezone v ligi

#občasno se izvajajo tudi turnirji, ki so v drugačni obliki kot lige
turnirji_format = [("_Season_World_Championship", 2014, 2017), 
                   ("_Season_World_Championship/Main_Event", 2017, 2024),
                   ("_Mid-Season_Invitational", 2015, 2020), 
                   ("_Mid-Season_Invitational", 2021, 2024)

]





for liga in lige_format:
    for leto in range(liga[1], liga[2]):
        for del_sezone in liga[3]:
            linki.append(f'https://lol.fandom.com/wiki/{liga[0]}/{leto}_Season/{del_sezone}/Match_History')


for turnir in turnirji_format:
    for leto in range(turnir[1], turnir[2]):
        linki.append(f'https://lol.fandom.com/wiki/{leto}{turnir[0]}/Match_History')
def download_url_to_string(url):
    try:
        page_content = requests.get(url)
    except requests.exceptions.RequestException:   
        print("Spletna stran ni dosegljiva")
        return None
    return page_content.text 
for link in linki:   #preverimo, če so vsi linki v redu
    if download_url_to_string(link) == None:
        print(link)
