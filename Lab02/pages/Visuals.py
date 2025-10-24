# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Social Media Data Visualizations 📈")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.write("**Raw CSV Data**")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    current_data_df = pd.read_csv('data.csv')
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")


try:
    with open("data.json", "r") as file:
        sampleData = json.load(file)

except FileNotFoundError:
    st.warning("The 'data.json' file is empty or does not exist yet.")

# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.



st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Static: Histogram of Social Media Hours") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.


hours = pd.Series(current_data_df.values.flatten())
new_hours = pd.to_numeric(hours, errors='coerce')
updated_hours = new_hours.dropna()

hist_data = updated_hours.value_counts().sort_index()

st.bar_chart(hist_data)




st.write("This graph shows the frequency of the amount of hours spent on social media in a day for a week.")

# GRAPH 2: DYNAMIC GRAPH
st.subheader("Dynamic: Line Graph by Day Range ") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:dont
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

current_data_df['Category'] = pd.Categorical(current_data_df['Category'], categories=days, ordered=True)

day_num = {}
for i in range(len(days)):
    day = days[i]
    day_num[day] = i

    #print(day_num)

day_nums = []
for day in current_data_df['Category']:
    num = day_num[day] 
    day_nums.append(num)
    
start, end = st.slider("Select day range", 0, 6, (0, 6)) #NEW

rangeDays = list(range(start, end +1))
finalDf = current_data_df[current_data_df["Category"].isin(rangeDays)]

st.line_chart(finalDf["Value"])

st.write("This graph shows you your data represented in a line graph according to the day range you set it at.")

# GRAPH 3: DYNAMIC GRAPH
st.subheader("Dynamic: JSON Data - Hours spent on Social Media vs Level of Productivity") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.


newDf = pd.DataFrame(sampleData["data_points"])

newDf['hours'] = pd.to_numeric(newDf['hours'])
newDf = newDf.sort_values('hours')                          

st.line_chart(newDf['value'])




