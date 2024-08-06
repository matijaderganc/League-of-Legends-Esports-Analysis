
import csv
import os
import requests 
import re
from bs4 import BeautifulSoup


test = []



def zaokrozi(x, baza=50):
    return baza * round(x/baza)

print(zaokrozi(126))

