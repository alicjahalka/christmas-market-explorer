import pandas as pd
analyze_markets = pd.read_csv('data/processed/christmas_markets_clean.csv')
analyze_markets['start_date'] = pd.to_datetime(analyze_markets['start_date'], errors='coerce')
analyze_markets['end_date'] = pd.to_datetime(analyze_markets['end_date'], errors='coerce')

def selected_date (your_date):
    your_date = pd.to_datetime(your_date)
    opened_christmas_markets = analyze_markets[
        (analyze_markets['start_date'] <= your_date) & (analyze_markets['end_date'] >= your_date)]

    if len(opened_christmas_markets)==0:
        print('CLOSED CHRISTMAS MARKET')

    return opened_christmas_markets

while True:
    user_choice = input('Choose an option (1-4): ')

    if user_choice=='1':
        earliest_christmas_markets = pd.read_csv(r'data/processed/earliest_christmas_markets_2026.csv')
        print(earliest_christmas_markets.head(10))
    elif user_choice == '2':
        earliest_markets_by_country2026 = pd.read_csv(r'data/processed/earliest_christmas_markets_by_country_2026.csv')
        print(earliest_markets_by_country2026.head(50))
    elif user_choice =='3':
        user_date =input('Enter a date (YYYY-MM-DD): ')
        open_christmas_markets2026 = selected_date(user_date)
        print(open_christmas_markets2026.head(50))

    elif user_choice == '4':
        print('Exit')
        break
    else:
        print('Invalid option. Please choose 1-4.')
