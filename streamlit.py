import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set page configuration
st.set_page_config(page_title="House Pricing Dashboard", layout="wide", initial_sidebar_state="expanded")

# App title
st.title("🏡 House Pricing Dashboard")
st.image("house.jpg")

# Sidebar section
st.sidebar.title("Control Panel")
st.sidebar.markdown("Use the controls below to filter the data:")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("kc_house_data.csv")
    return df

df = load_data()

# Sample data to avoid overloading
df_sampled = df.sample(frac=0.2)

# Sidebar Filters
st.sidebar.subheader("Filter by")
bedrooms = st.sidebar.slider("Number of Bedrooms", min_value=int(df['bedrooms'].min()), max_value=int(df['bedrooms'].max()), value=(int(df['bedrooms'].min()), int(df['bedrooms'].max())))

price_range = st.sidebar.slider("Price Range", min_value=int(df['price'].min()), max_value=int(df['price'].max()), value=(int(df['price'].min()), int(df['price'].max())))

sqft_living = st.sidebar.slider("Living Area (sqft)", min_value=int(df['sqft_living'].min()), max_value=int(df['sqft_living'].max()), value=(int(df['sqft_living'].min()), int(df['sqft_living'].max())))

# Apply filters
df_filtered = df_sampled[
    (df_sampled['bedrooms'].between(bedrooms[0], bedrooms[1])) &
    (df_sampled['price'].between(price_range[0], price_range[1])) &
    (df_sampled['sqft_living'].between(sqft_living[0], sqft_living[1]))
]

# Display filtered data in the main page
st.subheader("Filtered House Listings")
st.write(f"Displaying {len(df_filtered)} houses based on your filters")
st.dataframe(df_filtered)

# Main content - Visualizations
st.header("House Data Insights")

# Row with 3 columns
col1, col2, col3 = st.columns(3)

# First column - Price distribution
with col1:
    st.subheader("Price Distribution")
    plt.figure(figsize=(5,4))
    sns.histplot(df_filtered['price'], kde=True, color='purple')
    plt.title("Price Distribution", fontsize=12)
    st.pyplot()

# Second column - Bedrooms vs Price
with col2:
    st.subheader("Bedrooms vs Price")
    plt.figure(figsize=(5,4))
    sns.boxplot(x='bedrooms', y='price', data=df_filtered, palette="coolwarm")
    plt.title("Price by Number of Bedrooms", fontsize=12)
    st.pyplot()

# Third column - Living Area vs Price
with col3:
    st.subheader("Living Area vs Price")
    plt.figure(figsize=(5,4))
    sns.scatterplot(x='sqft_living', y='price', data=df_filtered, hue='bedrooms', palette='Spectral', alpha=0.7)
    plt.title("Living Area (sqft) vs Price", fontsize=12)
    st.pyplot()

# Map of house locations
st.header("Map of House Locations")
st.map()

# Interactive Widgets
st.sidebar.header("Interactive Widgets")
st.sidebar.subheader("Test Some Widgets")

# Button
if st.sidebar.button("Buy a House"):
    st.sidebar.success("Congratulations! You've bought a house 🎉")

# Text Input
name = st.sidebar.text_input("Enter Your Name")
if name:
    st.sidebar.write(f"Welcome, {name}!")

# Text Area Input
address = st.sidebar.text_area("Enter Your Address")
if address:
    st.sidebar.write(f"Address: {address}")

# Date and Time Input
selected_date = st.sidebar.date_input("Select a Date:")
st.sidebar.write(f"Selected Date: {selected_date}")

selected_time = st.sidebar.time_input("Select Time:")
st.sidebar.write(f"Selected Time: {selected_time}")

# Checkbox
if st.sidebar.checkbox("I accept the terms and conditions"):
    st.sidebar.write("Thank you for accepting the terms.")

# Slider for Age
age = st.sidebar.slider("Select your age", min_value=18, max_value=60, value=30)
st.sidebar.write(f"Selected Age: {age}")

# Conclusion
st.sidebar.markdown("---")
st.sidebar.markdown("This dashboard provides insights on house pricing data from King County. Feel free to explore the data using the filters and widgets above.")
st.video("https://www.youtube.com/watch?v=4jnzf1yj48M")
# Footer
st.markdown("---")
st.markdown("#### Powered by Streamlit | Data from King County House Sales | Developed by Swapan")
