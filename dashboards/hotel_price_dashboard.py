import os
import pandas as pd
import streamlit as st
import plotly.express as px

# Title
st.title("🏨 Hotel Price Prediction Dashboard")
st.caption("AI-based forecasting of hotel prices for upcoming days")

# Load predictions
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "predictions",
    "future_hotel_predictions.csv"
)

pred_df = pd.read_csv(csv_path)
pred_df["date"] = pd.to_datetime(pred_df["date"])
hotels = pred_df["hotel"].unique()


# Sidebar filters
st.sidebar.header("🔎 Filters")

selected_hotels = st.sidebar.multiselect(
    "Select Hotel(s)",
    hotels,
    default=hotels[:2]
)

# date column
pred_df['date'] = pd.to_datetime(pred_df['date'])

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(pred_df['date'].min(), pred_df['date'].max()),
    min_value=pred_df['date'].min(),
    max_value=pred_df['date'].max()
)

#filter hotels
filtered_df = pred_df[
    (pred_df["hotel"].isin(selected_hotels)) &
    (pred_df["date"] >= pd.to_datetime(date_range[0])) &
    (pred_df["date"] <= pd.to_datetime(date_range[1]))]

# Find the cheapest predicted hotel in the filtered data

if filtered_df.empty:
    st.warning("No data available for the selected date range.")
else:
    # Metrics
    avg_price = filtered_df['predicted_price'].mean()
    min_price = filtered_df['predicted_price'].min()
    max_price = filtered_df['predicted_price'].max()

    col1, col2, col3 = st.columns(3)
    col1.metric("Average Price", f"${avg_price:.2f}")
    col2.metric("Minimum Price", f"${min_price:.2f}")
    col3.metric("Maximum Price", f"${max_price:.2f}")

    # Cheapest & most expensive hotels
    try:
        cheapest = filtered_df.loc[filtered_df['predicted_price'].idxmin()]
        most_expensive = filtered_df.loc[filtered_df['predicted_price'].idxmax()]

        st.write(f"💡 **Cheapest predicted hotel**: {cheapest['hotel']} at ${cheapest['predicted_price']:.2f}")
        st.write(f"💡 **Most expensive predicted hotel**: {most_expensive['hotel']} at ${most_expensive['predicted_price']:.2f}")
    except ValueError:
        st.warning("No hotels available to display cheapest/most expensive info.")


#filtered data table
st.subheader("Filtered Predicted Prices")
st.dataframe(filtered_df.style.background_gradient(subset=['predicted_price'], cmap='YlGnBu'))


#plot
st.subheader("Price Trends")
fig = px.line(
    filtered_df,
    x="date",
    y="predicted_price",
    color="hotel",
    markers=True,
    hover_data={'predicted_price': ':.2f'}
)
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Predicted Price ($)",
    legend_title="Hotel",
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)


st.info(
    f"💡 **Cheapest predicted hotel**: {cheapest['hotel']} "
    f"on {cheapest['date'].date()} "
    f"for €{cheapest['predicted_price']:.2f}"
)

st.divider()
st.markdown("""
### 📌 About this dashboard
This dashboard visualizes **AI-based hotel price predictions**
generated using a machine learning model trained on historical pricing data.

**Tech stack:**  
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Plotly
""")



