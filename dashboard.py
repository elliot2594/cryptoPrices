import csv 
import sqlite3
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development



def createCSV():
	db_file = 'crypto.db'
	with sqlite3.connect(db_file) as conn:
	       # conn.row_factory = lambda cursor, row: row[0]
	        cur = conn.cursor()
	        cur.execute("SELECT date, price FROM solana")
	        data = cur.fetchall()
	        print(data)
	with open('values.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(['Date', 'Prices'])
		writer.writerows(data)


if __name__== '__main__':
	df = pd.read_csv('values.csv')
	st.set_page_config(
		page_title="Real-Time Solana Dashboard",
		layout="wide"
	)
	placeholder = st.empty()
	with placeholder.container():
		fig_col1, fig_col2 = st.columns(2)

		with fig_col1:
			st.markdown("### Solana")
			fig = px.line(data_frame=df, y="Prices", x="Date")
			st.write(fig)

		st.dataframe(df)