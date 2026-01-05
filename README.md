# Hotel Price Forecasting

**Hotel Price Forecasting** is a Python-based project that predicts daily hotel prices using machine learning. The project includes data collection, preprocessing, analysis, and a Streamlit dashboard for visualization.

---

## Features

* **Data Analysis:** Explore and visualize hotel pricing trends.
* **Price Prediction:** Predict future hotel prices using a trained `RandomForestRegressor` model.
* **Interactive Dashboard:** Filter by hotel and date range to view predicted prices in a user-friendly interface.
* **Dummy Data:** A sample dataset is provided for testing and demonstration purposes. Users can fetch real data from the API if they have a valid API key.

---

## Project Structure

```
Hotel-Price-Forecasting/
│
├── data/
│   ├── processed/           # Preprocessed CSV datasets
│   └── raw/                 # Raw or fetched data
│
├── dashboards/              # Streamlit dashboard scripts
│   └── hotel_price_dashboard.py
│
├── models/                  # Trained machine learning models
│   └── hotel_price_model.pkl
│
├── src/                     # Python scripts for data fetching, preprocessing, and modeling
│   ├── fetchdata.py
│   └── transform.py
│
├── notebooks/               # Jupyter notebooks
│   ├── data_analysis.ipynb
│   └── price_prediction.ipynb
│
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

* Python 3.13+
* Streamlit
* pandas, numpy, scikit-learn, plotly

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Using Your Own API Key

To fetch real hotel price data:

1. Replace the dummy dataset in `data/processed/` with your API call.
2. Add your API key in `fetchdata.py`:

```python
api_key = "YOUR_API_KEY_HERE"
```

3. Run the script to fetch and preprocess data:

```bash
python src/fetchdata.py
python src/transform.py
```

> **Note:** This project currently includes **dummy data** because the API key has expired. You can replace it with your own key to fetch live data.

---

### Run the Dashboard

Start the Streamlit dashboard:

```bash
streamlit run dashboards/hotel_price_dashboard.py
```

* Use the sidebar to select hotels and a date range.
* View metrics, trends, and predicted prices interactively.

---

### Predictions

The model predicts daily hotel prices for the next 7 days for selected hotels. Predictions are stored in:

```
predictions/future_hotel_predictions.csv
```

---

### License

This project is for **educational purposes**. Feel free to modify and reuse the code for personal projects.

---

### Contact

**Mahe Noor** – [GitHub](https://github.com/Mahe7Noor) | Email: [mahenoor.work@gmail.com](mailto:mahenoor.work@gmail.com)

---

