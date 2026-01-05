import pandas as pd
import numpy as np
from datetime import datetime, timedelta

#hotel info
hotels = [
    {"hotel": "Doubletree By Hilton New York Downtown", "rating": 3.5},
    {"hotel": "Motto by Hilton New York City Chelsea", "rating": 4.8},
    {"hotel": "The Evelyn Hotel", "rating": 4.8},
    {"hotel": "Embassy Suites By Hilton Times Square", "rating": 4.1},
]

# Generates dummy data for 30 days
start_date = datetime(2025, 12, 1)
data = []

for hotel in hotels:
    for i in range(30):  # 30 days
        date = start_date + timedelta(days=i)
        price = round(100 + 200 * np.random.rand(), 2)  # random price between 100 and 300
        data.append({
            "hotel": hotel["hotel"],
            "rating": hotel["rating"],
            "price": price,
            "date": date.strftime("%Y-%m-%d")
        })

# Convert to DataFrame
df = pd.DataFrame(data)


# Save CSV
df.to_csv("../data/processed/hotel_prices_dummy.csv", index=False)
print("Dummy data saved to data/processed/hotel_prices_dummy.csv")
