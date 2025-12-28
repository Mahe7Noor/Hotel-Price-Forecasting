'''import os
import fetch_data
import pandas as pd

# Fetch data
data = fetch_data.fetch_hotels_price()

if not data:
    print("No data returned from API.")
    exit()

#remove the last item that it metadata
hotels = [h for h in data if isinstance(h, dict)]

rows = []

# For each hotel in your response
for hotel in data:
    hotel_name = hotel.get("name")
    hotel_id = hotel.get("hotelId")
    rating = hotel.get("reviews", {}).get("rating")
    review_count = hotel.get("reviews", {}).get("count")

    # Use vendor1/price1 directly
    vendor = hotel.get("vendor1") or "Unavailable"
    price = hotel.get("price1") or "Unavailable"

    rows.append({
        "hotel_name": hotel_name,
        "hotel_id": hotel_id,
        "rating": rating,
        "review_count": review_count,
        "vendor": vendor,
        "price": price
    })

df = pd.DataFrame(rows)

# Optional: add city & date info
df["city"] = "New York"

os.makedirs("data/processed", exist_ok=True)

with open("data/raw/hotels_prices.json", "w") as f:
    json.dump(response.json(), f)

# Now save the CSV
df.to_csv("data/processed/hotel_prices.csv", index=False)
print("Vendor-wise CSV saved successfully")'''
