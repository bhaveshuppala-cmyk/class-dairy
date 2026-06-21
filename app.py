import streamlit as st
import pandas as pd
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(layout="wide")
st.title("🏫 Digital Class Diary - Entry Portal")

# Setup Google Sheets connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# You will need to upload your service account JSON file to GitHub for this to work
creds = ServiceAccountCredentials.from_json_keyfile_name('secrets.json', scope)
client = gspread.authorize(creds)
sheet = client.open("YourSheetName").sheet1

# Entry Form
with st.sidebar.expander("Teacher Entry"):
    with st.form("entry_form"):
        cls = st.text_input("Class")
        sec = st.text_input("Section")
        sub = st.text_input("Subject")
        cw = st.text_area("Classwork")
        hw = st.text_area("Homework")
        submit = st.form_submit_button("Save Entry")
        
        if submit:
            sheet.append_row([cls, sec, str(date.today()), sub, cw, hw])
            st.success("Entry Saved!")

# Display Data (same as before)
# ... (rest of your display code)
