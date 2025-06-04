import pandas as pd
import re

# Load the raw CSV file
df = pd.read_csv('f1_driver_standings_2024.csv')

# Drop duplicate headers and rows with "Sources"
df = df[df['Pos.'] != 'Pos.']
df = df[~df.iloc[:, 0].astype(str).str.contains('Sources', na=False)]
df = df.dropna(how='all')

# Clean race result values
def extract_result(cell):
    if pd.isna(cell):
        return pd.NA, pd.NA
    text = str(cell)
    match = re.search(r'(\d+)', text)
    position = int(match.group(1)) if match else pd.NA
    notes = re.sub(r'\d+', '', text).strip()
    return position, notes

# Keep main columns
clean_df = df[['Pos.', 'Driver', 'Points']].copy()

# Clean all race columns
race_columns = [col for col in df.columns if col not in ['Pos.', 'Driver', 'Points']]
for race in race_columns:
    pos_col = []
    note_col = []
    for val in df[race]:
        pos, note = extract_result(val)
        pos_col.append(pos)
        note_col.append(note)
    clean_df[f'{race}_pos'] = pos_col
    clean_df[f'{race}_note'] = note_col


clean_df.to_csv('cleaned_f1_driver_standings_2024.csv', index=False)
print(" Cleaned data saved as 'cleaned_f1_driver_standings_2024.csv'")
