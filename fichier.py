#---------- EXERCICE 2 ----------#

import requests
from bs4 import BeautifulSoup
import csv

# ÉTAPE 1 : Créer un fichier result.csv pour écrire les données filtrées, encodage UTF-8
result_file = open("result.csv", "w", encoding="utf-8")
writer = csv.writer(result_file, delimiter=",")
header = ["Team", "Country", "Year", "Wins", "Losses", "Draws", "Goals For (GF)", "Goals Against (GA)", "+/-"]

writer.writerow(header)

# ÉTAPE 2 : Parcourir les dix premières pages du site
for i in range(1, 11):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr", class_="team")

    # ÉTAPE 3 :Vérifier si les données respectent les conditions demandées et les écrire dans result.csv
    for row in rows[1:]:
        data = [td.text.strip() for td in row.find_all("td")]
        goals_against = int(data[7].replace(".", ""))
        diff = int(data[8].replace(".", ""))
        if diff > 0 and goals_against < 300:
            writer.writerow(data)