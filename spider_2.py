import logging
import scrapy
import json
import os
from scrapy.crawler import CrawlerProcess
import re


class Bookingspider2(scrapy.Spider):
    name = 'bookingspider2'

    def start_requests(self):
        # Récupérer le répertoire où se trouve le script Python
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Le répertoire du script
        file_path = os.path.join(script_dir, 'hotels_liste.json')  # Le fichier JSON dans le même répertoire que le script
        
        # Vérifier si le fichier existe
        if not os.path.exists(file_path):
            logging.error(f"Le fichier {file_path} n'existe pas !")
            return  # Arrêter l'exécution du spider si le fichier n'existe pas
        else:
            logging.info(f"Le fichier {file_path} existe. Début du traitement.")

        # Charger les données du fichier JSON contenant les URL des hôtels
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Vérifier si des données ont été lues
        if not data:
            logging.error("Le fichier JSON est vide ou n'a pas pu être lu.")
            return

        # Pour chaque hôtel, envoyer une requête vers l'URL de l'hôtel
        for hotel in data:
            url_hotel = hotel['url']
            logging.info(f"Envoi de la requête pour l'URL de l'hôtel : {url_hotel}")
            yield scrapy.Request(url=url_hotel, callback=self.parse_hotel_details, meta={
                'city': hotel['city'],
                'nom': hotel['nom'],
                'note': hotel['note'],
                'url': url_hotel
            })

    def parse_hotel_details(self, response):
        # Log de la réponse
        logging.info(f"Réponse reçue pour l'URL: {response.url}")
        
        # Récupérer l'adresse de l'hôtel à l'aide du sélecteur CSS
        adresse = response.css("div.a53cbfa6de.f17adf7576::text").get()  
        if adresse:
            adresse = adresse.strip()
        
        # Récupérer les coordonnées GPS (latitude et longitude)
        latlng = response.css('a[data-atlas-latlng]::attr(data-atlas-latlng)').get()

       
        # Récupérer les points forts de l'hôtel
        points_forts = response.css("div.e1eebb6a1e.e6208ee469.d0caee4251::text").getall()  
        points_forts = [point.strip() for point in points_forts if point.strip()]

        # Vérification des données extraites
        #logging.info(f"Adresse: {adresse}, Latitude: {latitude}, Longitude: {longitude}, Points forts: {points_forts}")

        # Renvoyer toutes les informations extraites sous forme de dictionnaire
        yield {
            'city': response.meta['city'],         # Ville de l'hôtel
            'nom': response.meta['nom'],           # Nom de l'hôtel
            'url': response.meta['url'],           # URL de l'hôtel
            'note': response.meta['note'],         # Note de l'hôtel
            'latlong': latlng,                  # Latitude et longitude de l'hôtel
            'adresse': adresse,                    # Adresse de l'hôtel
            'points_forts': points_forts          # Points forts de l'hôtel
        }

# Configuration du processus Scrapy

#export vers repertoire de travail
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, 'hotels_liste_details.json')

print(f"[INFO] Le fichier sera enregistré ici : {output_file}")

process = CrawlerProcess(settings={
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'FEEDS': {output_file: {'format': 'json', 'encoding': 'utf-8'}},
    'DOWNLOAD_DELAY': 1,
    'LOG_LEVEL': 'DEBUG'
    })

process.crawl(Bookingspider2)
process.start()