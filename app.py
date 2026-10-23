import streamlit as st
import pandas as pd


st.title("Smart Temperature Monitoring System")

st.write("Arduino Uno + DHT22 Sensor Simulation")

st.subheader("Temperature Monitor")

temperature = st.slider(
    "Adjust Temperature (°C)",
    min_value=20,
    max_value=50,
    value=24
)

st.metric("Temperature", f"{temperature} °C")

if temperature >= 40:
    st.error("WARNING! High Temperature")
    st.write("Red LED: ON")
else:
    st.success("Normal Temperature")
    st.write("Red LED: OFF")

st.subheader("Wokwi Temperature Test Results")

data = pd.DataFrame({
    "Temperature": [24, 30, 35, 39, 40, 42, 45],
    "LED Status": [
        "OFF", "OFF", "OFF", "OFF",
        "ON", "ON", "ON"
    ]
})

st.dataframe(data)

st.subheader("Temperature Graph")

st.line_chart(
    data,
    y="Temperature"
)

st.subheader("Interpretation")

st.write(
    "The warning LED turns ON when the "
    "temperature reaches 40°C or higher. "
    "Below 40°C, the LED remains OFF."
)
