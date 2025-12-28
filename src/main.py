'''import requests

def fetch_hotels_price():
    url = "https://api.makcorps.com/city"
    params = {
        'cityid': '60763',
        'pagination': '0',
        'cur': 'USD',
        'rooms': '1',
        'adults': '2',
        'checkin': '2026-01-28',
        'checkout': '2026-01-29',
        'api_key': 'HOTEL_API_KEY'
    }

    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        print(data)
        return data if data else []

    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}, {response.text}")
        return []

if __name__ == "__main__":
    data = fetch_hotels()
    print(data)'''
