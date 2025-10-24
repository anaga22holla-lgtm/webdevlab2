# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Social Media Collection Survey 📝")
st.write("Please enter hours spent on social media for each day of the week.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    monday_input = st.number_input("Monday:",
        min_value = 0.0,
        max_value = 24.0,
        step = 0.5                          
        )
    tuesday_input = st.number_input("Tuesday:",
        min_value = 0.0,
        max_value = 24.0,
        step = 0.5   
        )
    wednesday_input = st.number_input("Wednesday:",
        min_value = 0.0,
        max_value = 24.0,
        step = 0.5   
        )
    thursday_input = st.number_input("Thursday:",
        min_value = 0.0,
        max_value = 24.0,
        step = 0.5   
        )
    friday_input = st.number_input("Friday:",
        min_value = 0.0,
        max_value = 24.0,
        step = 0.5   
        )
    sat_input = st.number_input("Saturday:",
        min_value = 0.0,
        max_value = 24.0,
        step = 0.5   
        )
    sun_input = st.number_input("Sunday:",
        min_value = 0.0,
        max_value = 24.0,
        step = 0.5   
        )
    #value_input = st.text_input("Enter a corresponding value:")

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        # --- YOUR LOGIC GOES HERE ---
        # TO DO:
        # 1. Create a new row of data from 'category_input' and 'value_input'.
        # 2. Append this new row to the 'data.csv' file.
        #    - You can use pandas or Python's built-in 'csv' module.
        #    - Make sure to open the file in 'append' mode ('a').
        #    - Don't forget to add a newline character '\n' at the end.
        data = pd.DataFrame({
            "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "Hours": [monday_input, tuesday_input, wednesday_input, thursday_input, friday_input, sat_input, sun_input]
        })

        file = os.path.exists("data.csv")
        data.to_csv("data.csv", mode = 'a', header = not file)

        
        
        st.success("Your data has been submitted! Go to the Visuals page to see graphs.")
        


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
