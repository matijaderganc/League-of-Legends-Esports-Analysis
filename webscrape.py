import csv
import os
import requests 
import re
from bs4 import BeautifulSoup

leta = range(2019, 2024)
linki = []
linki = []
lige_format = [("LEC", 2019, 2024, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("EU_LCS", 2014, 2019, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("NA_LCS", 2014, 2019, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("LCS", 2019, 2021, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs']),
               ("LCS", 2021, 2022, ['Spring_Season', 'Lock_In', 'Mid-Season_Showdown', 'Summer_Season', 'Championship']),
               ("LCS", 2022, 2024, ['Spring_Season', 'Lock_In', 'Spring_Playoffs', 'Summer_Season', 'Championship']),
               ("LCK", 2016, 2024, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs', 'Regional_Finals']),
               ("LPL", 2014, 2024, ['Spring_Season', 'Spring_Playoffs', 'Summer_Season', 'Summer_Playoffs', 'Regional_Finals']),
               ]
#ime lige, začetek, konec, deli sezone v ligi

#občasno se izvajajo tudi turnirji, ki so v drugačni obliki kot lige
turnirji_format = [("_Season_World_Championship", 2014, 2017), 
                   ("_Season_World_Championship/Main_Event", 2017, 2024),
                   ("_Mid-Season_Invitational", 2015, 2017),
                    ("_Mid-Season_Invitational/Main_Event", 2017, 2020),
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

def save_string_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename) #dobimo pot do datoteke
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

def save_frontpage(page, directory, filename):
    text = download_url_to_string(page)
    save_string_to_file(text, directory, filename)

#n = 0        #ta del kode naloži html datoteke
#for link in linki:
#    save_frontpage(link, "igre_podatki", f"{n}.html")
#    n += 1
zgodovina = {}
stevilo_iger = 0
for i in range(len(linki)):
    igre = []
    try:
        with open(f"igre_podatki/{i}.html") as dat:
            besedilo = dat.read()
            soup = BeautifulSoup(besedilo, "html.parser")

        tabela = soup.find('table', {'class': 'wikitable'}) #poiščemo tabelo z zgodovino iger
        vrstice = tabela.find_all('tr')[1:]  #spravimo tabelo v vrstice, izpustimo prvo
        for vrstica in vrstice:
            stolpci = vrstica.find_all('td')
            if len(stolpci) >= 5:  #preverimo, če imamo dovolj veliko tabelox
                date = stolpci[0].text.strip()
                patch = stolpci[1].text.strip()
                blue_team = stolpci[2].find('a')['title'].strip()
                red_team = stolpci[3].find('a')['title'].strip()
                winner = stolpci[4].find('a')['title'].strip()
                blue_roster = stolpci[9].text.strip()
                red_roster = stolpci[10].text.strip()
                igre.append((date, patch, blue_team, red_team, winner, blue_roster.split(","), red_roster.split(",")))
        zgodovina[i] = igre
        stevilo_iger += len(igre)
    except:
        print(f"{i} ni veljaven")
print(igre)
print(stevilo_iger)

