# Kayak Project - Coastal Tourism Weather & Hotel Analysis

## 📄 Description

This project aims to centralize, process, and visualize weather and hotel data for several French coastal cities. The final goal is to build an application that allows users to easily explore:

- Upcoming weather (temperature, wind, sunshine)
- Top-rated hotels available
- An interactive map based on user-selected criteria (bonus)

## 🧱 Modular Architecture

The project is now structured into **3 independent notebooks**:

### 1. `kayack_data.ipynb` — Data Acquisition

- Retrieve GPS coordinates via Nominatim API
- Collect weather data from OpenWeather API
- Scrape hotel listings using Scrapy spiders
- Save and export `.csv` files to AWS S3
- Bonus: generate weather maps using Folium

### 2. `kayack_sql.ipynb` — ETL Pipeline

- Separate pipelines for the 3 sources: City / Hotels / Weather
- Cleaning, transforming, and normalizing datasets
- Final merge into a unified dataset
- Export to SQL or final CSV

### 3. `kayack_top_5.ipynb` — User Interface

- User input: city, date, desired weather conditions
- Generate top 5 best cities with hotels available
- Interactive map rendering (temperature, weather, wind)

## 🚀 Technologies & Tools

- **Python 3.10+**
- **Pandas / Numpy**: data manipulation
- **Folium**: map visualizations
- **Requests**: API requests
- **Scrapy**: hotel web scraping
- **OpenWeatherMap API**: 5-day weather forecast
- **Nominatim API (OpenStreetMap)**: GPS geocoding
- **AWS S3**: cloud storage for `.csv` files
- **.env**: secure API key management

## 🛠️ How to Run the Project

1. Clone this repository
2. Create a `.env` file at the root directory with your API keys:

```bash
OPENWEATHER_API_KEY=...
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

3. Run the notebooks in this order:
   - `kayack_data.ipynb`
   - `kayack_sql.ipynb`
   - `kayack_top_5.ipynb`

## 🌟 Next Steps

- Full integration into a **Streamlit interface**
- Web deployment (via streamlit.io or Docker container)
- Add a **global recommendation score** per city (weather + hotel quality)
- Implement **dynamic filtering** (price, stars, weather preferences)

---

Created as part of the "Kayak Intelligent Tourism" project ✨

