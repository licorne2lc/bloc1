# Projet Kayak - Analyse Météo et Hôtels pour Tourisme

## 📄 Description

Ce projet vise à centraliser, traiter et visualiser des données météorologiques et hôtelières pour plusieurs villes côtières françaises. L'objectif est de proposer une application permettant à un utilisateur de consulter facilement :

- La météo à venir (température, vent, ensoleillement)
- Les meilleurs hôtels disponibles
- Une carte interactive selon ses critères (bonus)

## 🧱 Architecture modulaire

Le projet est désormais structuré en **3 notebooks indépendants** :

### 1. `kayack_data.ipynb` — Acquisition des données

- Récupération des coordonnées GPS via Nominatim
- Données météo via OpenWeather
- Scraping des hôtels (spiders Scrapy)
- Génération et export des fichiers `.csv` vers AWS S3
- Bonus : visualisation de cartes météo (Folium)

### 2. `kayack_sql.ipynb` — Pipeline ETL

- Traitement séparé des 3 canaux : City / Hotels / Weather
- Nettoyage, transformation, normalisation
- Fusion finale des données
- Export SQL ou CSV final

### 3. `kayack_top_5.ipynb` — Interface utilisateur

- Choix utilisateur (ville, date, météo souhaitée)
- Sélection du top 5 des villes avec hôtels disponibles
- Affichage des cartes interactives (température, météo, vent)

## 🚀 Technologies et outils utilisés

- **Python 3.10+**
- **Pandas / Numpy** : traitement de données
- **Folium** : visualisation cartographique
- **Requests** : accès aux APIs
- **Scrapy** : scraping hôtelier
- **OpenWeatherMap API** : données météo 5 jours
- **Nominatim API (OpenStreetMap)** : géocodage GPS
- **AWS S3** : stockage cloud des fichiers .csv
- **.env** : gestion sécurisée des clés API

## 🛠️ Exécution du projet

1. Cloner ce dépôt
2. Créer un fichier `.env` à la racine avec vos clés API :

```bash
OPENWEATHER_API_KEY=...
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

3. Lancer les notebooks dans cet ordre :
   - `kayack_data.ipynb`
   - `kayack_sql.ipynb`
   - `kayack_top_5.ipynb`

## 🌟 Prochaines évolutions

- Intégration complète dans une **interface Streamlit**
- Déploiement sur le web (streamlit.io ou conteneur Docker)
- Ajout d’un **score de recommandation global** par ville selon météo + hôtellerie
- Système de **filtrage dynamique** (prix, étoiles, météo personnalisée)

---

Réalisé dans le cadre du projet "Kayak Tourisme Intelligent" ✨

