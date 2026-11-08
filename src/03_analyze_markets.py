import pandas as pd
from numpy.typing.mypy_plugin import plugin

analyze_markets = pd.read_csv(r'data/processed/christmas_markets_clean.csv')
print(analyze_markets.head())
analyze_markets.info()
analyze_markets['start_date'] = pd.to_datetime(analyze_markets['start_date'], errors='coerce')
analyze_markets['end_date'] = pd.to_datetime(analyze_markets['end_date'], errors='coerce')
earliest_date = analyze_markets[['name_en','city', 'country','start_date']].sort_values(by=['start_date']).head(10)
earliest_date.to_csv(r'data/processed/earliest_christmas_markets_2026.csv', index=False)
earliest_by_country = analyze_markets.groupby('country').agg({'start_date':'min'}).reset_index()
print(earliest_by_country.sort_values(by=['start_date'], ascending=True))
merge_earliest_christmas_markets = pd.merge(left=earliest_by_country, right=analyze_markets, on=['country','start_date'])
print(merge_earliest_christmas_markets.head())
earliest_markets_by_country = merge_earliest_christmas_markets[['country','name_en', 'city','start_date']].sort_values(by=['start_date'])
print(earliest_markets_by_country.head())
earliest_markets_by_country.to_csv(r'data/processed/earliest_christmas_markets_by_country_2026.csv', index=False)

print('\nMARKETS OPEN IN DEC 6TH')
selected_date = pd.to_datetime('2026-12-06')
open_christmas_markets = analyze_markets[(analyze_markets['start_date'] <= selected_date) & (analyze_markets['end_date'] >= selected_date)]
print(open_christmas_markets[['name_en','city','country','end_date','start_date']])
print(len(open_christmas_markets))



def selected_date (your_date):
    your_date = pd.to_datetime(your_date)
    opened_christmas_markets = analyze_markets[
        (analyze_markets['start_date'] <= your_date) & (analyze_markets['end_date'] >= your_date)]

    if len(opened_christmas_markets)==0:
        print('CLOSED CHRISTMAS MARKET')

    return opened_christmas_markets

december_markets = selected_date('2026-11-07')
print(december_markets.head())

numbers_of_markets_country = analyze_markets.groupby('country').agg({'id':'count'})
numbers_of_markets_country = numbers_of_markets_country.rename(columns={'id':'number_of_markets'})
numbers_of_markets_country = numbers_of_markets_country.sort_values(by=['number_of_markets'], ascending=False).reset_index()
print(numbers_of_markets_country.head())

print('AVG duration days')

avg_duration_days = analyze_markets.groupby('country').agg({'duration_days':'mean'}).sort_values(by=['duration_days'], ascending=False).reset_index()
avg_duration_days = avg_duration_days.rename(columns={'duration_days':'avg_duration_days_col'})
avg_duration_days['avg_duration_days_col'] = avg_duration_days['avg_duration_days_col'].round(2)
print(avg_duration_days.head(10))

print('selected_christmas_markets_Poland')

selected_christmas_markets_poland = analyze_markets[(analyze_markets['country']=='PL')
&
(analyze_markets['duration_days']>30)
&
(analyze_markets['start_date'] < pd.to_datetime('2026 - 12 - 01'))]

print(selected_christmas_markets_poland[['name_en','start_date','city','duration_days']])

print('selected_by_months')

analyze_markets['months']= analyze_markets['start_date'].dt.month
analyze_markets_by_months = analyze_markets.groupby('months').agg({'start_date':'count'}).sort_values(by='months', ascending=True)
analyze_markets_by_months = analyze_markets_by_months.reset_index()
analyze_markets_by_months = analyze_markets_by_months.rename(columns={'start_date':'start_by_months'})
print(analyze_markets_by_months)
analyze_markets_by_months.to_csv(r'data/processed/christmas_markets_by_month_2026.csv',index=False)
