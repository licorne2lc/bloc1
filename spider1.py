import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

villes = [
    "Mont Saint Michel", "St Malo", "Bayeux", "Le Havre", "Rouen", "Paris", "Amiens", "Lille", 
    "Strasbourg", "Chateau du Haut Koenigsbourg", "Colmar", "Eguisheim", "Besancon", "Dijon", 
    "Annecy", "Grenoble", "Lyon", "Gorges du Verdon", "Bormes les Mimosas", "Cassis", "Marseille", 
    "Aix en Provence", "Avignon", "Uzes", "Nimes", "Aigues Mortes", "Saintes Maries de la mer", 
    "Collioure", "Carcassonne", "Ariege", "Toulouse", "Montauban", "Biarritz", "Bayonne", "La Rochelle"
]

class Bookingspider1(scrapy.Spider):
    name = 'bookingspider1'

    def start_requests(self):
        # Itérer sur chaque ville pour créer l'URL de recherche
        for city in villes:
            url = f"https://www.booking.com/searchresults.fr.html?ss={city}&nflt=review_score%3D80"
            # Envoyer la requête pour cette URL avec la ville dans meta pour pouvoir l'utiliser dans parse
            yield scrapy.Request(url=url, callback=self.parse, meta={'city': city})

    def parse(self, response):
        # Extraire la liste des hôtels sur la page actuelle
        hotel_list = response.css("div[class='c066246e13 d8aec464ca']")

        # Itérer sur chaque hôtel dans la liste
        for hotel in hotel_list:
            # Extraire le nom de l'hôtel
            nom_hotel = hotel.css("div.f6431b446c.a15b38c233::text").get()
            if nom_hotel:
                nom_hotel = nom_hotel.strip()  # Enlever les espaces indésirables autour du nom

            # Extraire l'URL de l'hôtel
            url_hotel = hotel.css("div.c1edfbabcb h3 a::attr(href)").get()
            if url_hotel:
                url_hotel = response.urljoin(url_hotel)  # Convertir l'URL relative en absolue

            # Extraire la note de l'hôtel
            note_hotel = hotel.css("div.a3b8729ab1.d86cee9b25 ::text").get()
            if note_hotel:
                note_hotel = note_hotel[-4:].strip()  # Enlever les espaces autour de la note

            # Si l'un des champs est vide, on passe à l'hôtel suivant
            if not nom_hotel or not url_hotel or not note_hotel:
                continue

            # Renvoyer ces données sous forme de dictionnaire
            yield {
                'city': response.meta['city'],  # Récupérer la ville depuis meta
                'nom': nom_hotel,
                'url': url_hotel,
                'note': note_hotel
            }

# Configuration du processus Scrapy
process = CrawlerProcess(settings={
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',  # Définir l'agent utilisateur pour simuler un navigateur
    'FEEDS': {'D:/jedha/full_stack/projet/Scraping_Kayak/hotels_liste.json': {'format': 'json',
                                                                                'encoding': 'utf-8'}},  # Format de sortie du fichier
    'DOWNLOAD_DELAY': 1,  # Délai entre les requêtes
    'LOG_LEVEL': logging.INFO 
})

# Lancer le spider
process.crawl(Bookingspider1)
process.start()


