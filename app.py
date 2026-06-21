import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(layout="wide")
st.title("🏫 Digital Class Diary")

# Your Sheet ID
SHEET_ID = '1poKLqm-2ZxZw4Ax37TEB043X-My539MqJ5BQXnkLZPI'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=Sheet1'

@st.cache_data(ttl=60)
def load_data():
    return pd.read_csv(url)

df = load_data()

st.sidebar.header("Select Room")
sel_class = st.sidebar.selectbox("Class", sorted(df['Class'].unique()))
sel_sec = st.sidebar.selectbox("Section", sorted(df['Section'].unique()))

st.subheader(f"Schedule: Class {sel_class}-{sel_sec} | Date: {date.today()}")

# Filter to show today's data only
df['Date'] = pd.to_datetime(df['Date']).dt.date
view_data = df[(df['Class'] == sel_class) & 
               (df['Section'] == sel_sec) & 
               (df['Date'] == date.today())]

if not view_data.empty:
    for index, row in view_data.iterrows():
        st.markdown(f"### 📘 Subject: {row['Subject']}")
        col1, col2 = st.columns(2)
        col1.info(f"**Classwork:** {row['Classwork']}")
        col2.warning(f"**Homework:** {row['Homework']}")
        st.divider()
else:
    st.info("No entries for today.")
