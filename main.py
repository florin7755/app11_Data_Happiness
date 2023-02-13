import streamlit as st
from streamlit.web import cli as stcli
from streamlit import runtime
import sys
import plotly.express as px
import pandas as pd

# Add a title widget
st.title("In Search for Happiness")

# Add two select boxes
option_x = st.selectbox("Select the data for the X-axis",
                        ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the Y-axis",
                        ("GDP", "Happiness", "Generosity"))
#Load the dataframe
df = pd.read_csv("happy.csv")

# Match the value of the first option
match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

# Match the value of the second option
match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

# Add a subheader above the plot
st.subheader(f"{option_x} and {option_y}")

# Create and add the plot to the webpage
figure1 = px.scatter(x=x_array, y=y_array,
                     labels={"x": option_x, "y": option_y})
st.plotly_chart(figure1)

if __name__ == '__main__':
    if runtime.exists():
       name = tuple
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())