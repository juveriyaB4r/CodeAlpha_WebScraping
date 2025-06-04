import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

def main():
    url = "https://en.wikipedia.org/wiki/2024_Formula_One_World_Championship"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    tables = pd.read_html(StringIO(response.text))
    print(f"🔍 Found {len(tables)} tables")

    for idx, table in enumerate(tables):
        # Flatten MultiIndex columns if needed
        if isinstance(table.columns, pd.MultiIndex):
            flat_columns = [' '.join(col).strip().lower() for col in table.columns.values]
        else:
            flat_columns = [str(col).lower() for col in table.columns]

        # Check if it's likely the driver standings table
        if 'driver' in flat_columns and 'points' in flat_columns:
            print(f"✅ Found driver standings at table index {idx}: {table.columns.tolist()}")
            table.to_csv("f1_driver_standings_2024.csv", index=False)
            print("💾 Saved as f1_driver_standings_2024.csv")
            print(table.head())
            return

    print("❌ Driver standings table not found.")

if __name__ == "__main__":
    main()
