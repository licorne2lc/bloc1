# Projet Kayak - Construction d'une architecture de données

auteur : Jerome Moulinier 

## 📄 Description

Ce projet vise à centraliser, traiter et visualiser les données météo et hôtelières de plusieurs villes côtières françaises. 
L’objectif final est de construire une application permettant aux utilisateurs d’explorer facilement :

- La météo à venir (température, vent, ensoleillement)
    
- Les hôtels les mieux notés disponibles
    
- 2 cartes interactives basée sur les critères sélectionnés par l’utilisateur (bonus)

  ![image](https://github.com/user-attachments/assets/8b1afdd4-c743-4aa2-80ec-2f5f9ea1ba75)


## Architecture du projet

Le projet est structuré en 3 notebooks indépendants et 2 scripts Python :

### 1. kayack_data.ipynb — Acquisition des données
   
- Récupération des coordonnées GPS via l’API Nominatim

- Collecte des données météo via l’API OpenWeather

- Scraping des hôtels avec des spiders Scrapy

- Sauvegarde et export des fichiers .csv vers AWS S3

- Bonus : génération de cartes météo avec Folium

### 2. kayack_sql.ipynb — Pipeline ETL

  Pipelines séparés pour les 3 sources : Ville / Hôtels / Météo

- Nettoyage, transformation et normalisation des données.

- Export vers SQL et fichier CSV en local

- Fusion finale en un dataset unifié

![image](https://github.com/user-attachments/assets/2f07e7f5-6998-4b0f-a160-045e5392d78d)

### 3. kayack_top_5.ipynb — Interface Utilisateur
   
- Saisie utilisateur : Date + condition météo souhaitée parmi 3 choix : vent, chaleur ou soleil

- Génération du Top 5 des meilleures villes avec les 3 meilleurs hôtels disponibles

- Rendu interactif sur carte (températures, météo, vent)

### 4. Scripts spider (scraping Booking.com)
   
- Spider 1 → Liste de 20 hôtels par ville generation du fichier "hotels_liste.json"

- Spider 2 → Informations détaillées sur chaque hôtel "hotels_liste_details.json"

⚠️ Le scraping du site Booking.com a été réalisé dans un cadre strictement pédagogique et non commercial, dans le contexte de ma formation en science des données. Une attention particulière a été portée au respect des règles d'éthique du scraping, en limitant le volume de requêtes et en évitant toute surcharge des serveurs.

## Technologies & Tools

- **Python 3.10+**
- **Pandas / Numpy**: data manipulation
- **Folium**: map visualizations
- **Requests**: API requests
- **Scrapy**: hotel web scraping
- **OpenWeatherMap API**: 5-day weather forecast
- **Nominatim API (OpenStreetMap)**: GPS geocoding
- **AWS S3**: cloud storage for `.csv` files
- **.env**: secure API key management

## Démarrage rapide.

1. Clone this repository
2. Create a `.env` file at the root directory with your API keys:

```bash
OPENWEATHER_API_KEY=...
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

3. Run les notebooks dans cet ordre:
   - `kayack_data.ipynb`
   - `kayack_sql.ipynb`
   - `kayack_top_5.ipynb`

   Resultat avec 2 cartes:
   
    A. Map -->  top 5 des villes correspondant au criteres Date & la condition meteo recherché:
      
    ![image](https://github.com/user-attachments/assets/c7102867-83c7-42f8-94a8-561ac128f033)

    B. Map --> top 3 hotels pour les 5 villes.
   
   ![image](https://github.com/user-attachments/assets/fce335ad-8a3b-4d7a-a69a-dabc041df799)
   
   ![image](https://github.com/user-attachments/assets/39352737-2fe4-4319-9235-48a281923efc)

    c. Dataframe avec les details des 3 hotels pour les 5 villes.
   
    ![image](https://github.com/user-attachments/assets/de2ebfaa-0b60-4e68-8e39-9c731bf56168)



## Bonus 
Generation des cartes meteo suivant les 3 criteres de J+1 to J+8
### 1.Carte meteo

![image](https://github.com/user-attachments/assets/2ad7cde2-6d08-4772-99fe-1539b370e2c7)

### 2.Carte des temperatures.

![image](https://github.com/user-attachments/assets/7c9b4099-1d74-46bd-b5ef-8950482cc283)

###3.Carte des vents (force et orientation).

![image](https://github.com/user-attachments/assets/59036176-dd1f-4560-ba17-19edfe919a33)


## Next Steps

- Full integration into a **Streamlit interface**
- Web deployment (via streamlit.io or Docker container)
- Add a **global recommendation score** per city (weather + hotel quality)
- Implement **dynamic filtering** (price, stars, weather preferences)

---

