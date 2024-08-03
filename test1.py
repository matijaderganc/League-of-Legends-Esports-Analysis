
import csv
import os
import requests 
import re
from bs4 import BeautifulSoup


test = []
with open(f"igre_podatki/0.html") as dat:
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
        test.append((date, patch, blue_team, red_team, winner, blue_roster.split(","), red_roster.split(",")))
print(test)
