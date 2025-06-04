#  CodeAlpha - Web Scraping: F1 2024 Standings

This project scrapes live Formula 1 2024 driver standings from Wikipedia using Python, then cleans and structures the data for analysis.

# Tools Used
- `requests`
- `BeautifulSoup`
- `pandas`
- `re` (Regex for cleaning)

# Output Files
- `f1_driver_standings_2024.csv` → Raw scraped data from Wikipedia
- `cleaned_f1_driver_standings_2024.csv` → Cleaned, structured version for analysis

# How It Works
1. `f1_scraper.py` scrapes the 2024 F1 driver standings table from Wikipedia.
2. Saves it as `f1_driver_standings_2024.csv`.
3. `cleaned_scraper.py` processes the raw data:
   - Removes duplicate headers and irrelevant rows
   - Extracts position and notes from messy race data
   - Outputs a clean and structured CSV

# 🔗 Source
[Wikipedia - 2024 Formula One World Championship](https://en.wikipedia.org/wiki/2024_Formula_One_World_Championship)
