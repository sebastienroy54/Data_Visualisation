#!/usr/bin/env python3
import requests
import json
from datetime import datetime
import requests
import json
from datetime import datetime

def get_historical_data():
    # Récupérer l'historique des prix du Bitcoin en USD depuis CoinGecko
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

    params = {
        'vs_currency': 'usd',
        'days': 15,
        'interval': 'daily'
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Créer un fichier JSON avec des objets distincts pour chaque date
    with open('historic_data.json', 'w') as f:
        for i in range(len(data.get('prices', []))):
            date_timestamp = data['prices'][i][0]
            date_str = datetime.utcfromtimestamp(date_timestamp / 1000).strftime('%Y-%m-%d')

            daily_data = {
                "date": date_str,
                "prices": data['prices'][i][1],
                "market_caps": data['market_caps'][i][1],
                "total_volumes": data['total_volumes'][i][1],
            }

            # Check if the date has already been written to the file
            if i == 0 or date_str != datetime.utcfromtimestamp(data['prices'][i-1][0] / 1000).strftime('%Y-%m-%d'):
                f.write(json.dumps(daily_data, separators=(',', ':')) + '\n')

if __name__ == "__main__":
    get_historical_data()

