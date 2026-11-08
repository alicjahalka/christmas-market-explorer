import pandas as pd
markets=pd.read_csv(r'data/raw/christmas_markets_2026.csv')
print(markets.head())
print('\n CLEANING DATA')
markets_clean = markets.copy()
markets_clean['start_date'] = pd.to_datetime(markets_clean['start_date'],errors='coerce')
markets_clean['end_date'] = pd.to_datetime(markets_clean['end_date'],errors='coerce')
markets_clean['duration_days'] = markets_clean['end_date'] - markets_clean['start_date']
markets_clean['duration_days'] = markets_clean['duration_days'].dt.days
markets_clean['duration_days'] = markets_clean['duration_days'].astype('Int64')
markets_clean.to_csv(r'data/processed/christmas_markets_clean.csv', index=False)
