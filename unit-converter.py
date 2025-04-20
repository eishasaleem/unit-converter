import streamlit as st

st.title("🔄 Universal Unit Converter")

# Step 1: Select conversion category
category = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Step 2: Define units per category
units = {
    "Length": ['meters', 'kilometers', 'miles', 'feet'],
    "Weight": ['grams', 'kilograms', 'pounds', 'ounces'],
    "Temperature": ['celsius', 'fahrenheit', 'kelvin']
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value", value=0.0, format="%.2f")

# Step 3: Conversion functions
def convert_length(val, from_u, to_u):
    base = {'meters': 1, 'kilometers': 1000, 'miles': 1609.34, 'feet': 0.3048}
    return val * base[from_u] / base[to_u]

def convert_weight(val, from_u, to_u):
    base = {'grams': 1, 'kilograms': 1000, 'pounds': 453.592, 'ounces': 28.3495}
    return val * base[from_u] / base[to_u]

def convert_temperature(val, from_u, to_u):
    if from_u == to_u:
        return val
    # Convert to Celsius first
    if from_u == "fahrenheit":
        val = (val - 32) * 5/9
    elif from_u == "kelvin":
        val = val - 273.15
    # Now convert from Celsius to target
    if to_u == "fahrenheit":
        return val * 9/5 + 32
    elif to_u == "kelvin":
        return val + 273.15
    return val

# Step 4: Run conversion
if st.button("Convert"):
    if category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = "Unsupported"
    
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
