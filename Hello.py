import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import pytz
from suntime import Sun, SunTimeException


# Function to calculate sunlight duration
def sunlight_duration(lat, lon, date, timezone):
    sun = Sun(lat, lon)
    try:
        sunrise = sun.get_local_sunrise_time(date).astimezone(pytz.timezone(timezone))
        sunset = sun.get_local_sunset_time(date).astimezone(pytz.timezone(timezone))
        return sunset - sunrise
    except SunTimeException:
        return "Sun never sets/rises on this day"


# Streamlit app layout
st.title("Sunlight Duration Visualization")

# Inputs
lat = st.number_input("Latitude", value=40.71)  # Example: New York City
lon = st.number_input("Longitude", value=-74.01)
timezone = st.selectbox("Timezone", pytz.all_timezones, index=pytz.all_timezones.index('America/New_York'))
date = st.date_input("Date", value=datetime.now())

# Calculate sunlight duration
duration = sunlight_duration(lat, lon, date, timezone)
if isinstance(duration, timedelta):
    st.write(f"Sunlight duration on {date}: {duration}")
else:
    st.write(duration)

# Optional: Additional visualization or data display can be added here