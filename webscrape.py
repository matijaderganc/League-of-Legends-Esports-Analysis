import csv
import os
import requests 
from bs4 import BeautifulSoup

from leagues import turnirji_format, lige_format

linki = []
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

def url_v_string(url):
    try:
        page_content = requests.get(url)
    except requests.exceptions.RequestException:   
        print("Spletna stran ni dosegljiva")
        return None
    return page_content.text 

def string_v_datoteko(text, directory, ime):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ime) #dobimo pot do datoteke
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

def shrani_spletno_stran(page, directory, ime):
    text = url_v_string(page)
    string_v_datoteko(text, directory, ime)

odgovor = input('Če želite naložiti html datoteke napišite DA.')
if odgovor == 'DA':
    n = 0        #ta del kode naloži html datoteke
    for link in linki:
        shrani_spletno_stran(link, "igre_podatki", f"{n}.html")
        n += 1

vse_igre = []
for i in range(len(linki)):
    try:
        with open(f"igre_podatki/{i}.html", encoding = "utf-8") as dat:
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
                vse_igre.append((date, patch, blue_team, red_team, winner, blue_roster.split(","), red_roster.split(","), linki_lige[i])) #na seznam dodamo čas, patch (verzija igre), obe ekipi ter zmagovalca in pa igralce v ekipah
    except:
        print(f"{i} ni veljaven")
print(len(vse_igre))
os.makedirs("podatki_csv", exist_ok=True)
prva = ('Datum', 'Verzija', 'Modra_Stran', 'Rdeca_Stran', 'Zmagovalec', 'Modri_Igralci', 'Rdeci_Igralci', 'Liga')
with open("podatki_csv/igre.csv", "w", encoding = "utf-8") as dat:
    writer = csv.writer(dat)
    writer.writerow(prva)
    for igra in vse_igre:
        writer.writerow(igra)