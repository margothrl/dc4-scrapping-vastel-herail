#---------- EXERCICE 2 ----------#

import requests
from bs4 import BeautifulSoup
import csv

# ÉTAPE 1 : Créer un fichier result.csv pour écrire les données filtrées, encodage UTF-8
result_file = open("result.csv", "w", encoding="utf-8")
writer = csv.writer(result_file, delimiter=",")
header = ["Team", "Country", "Year", "Wins", "Losses", "Draws", "Goals For (GF)", "Goals Against (GA)", "+/-"]
