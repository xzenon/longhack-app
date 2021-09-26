import streamlit as st
import pandas as pd
import awesome_streamlit as ast

@st.cache
def load_data():
	data = pd.read_csv(
		"pages/csv/avg_lifespan_increase.csv",
		delimiter=',',
		names=['Compound name', 'Average lifespan increase'],
		skiprows=[0]
	)
	return data

def write():
	with st.spinner("Loading About ..."):
		st.title("Compounds database")
		st.subheader("Determine the average life span increase for a given compound across various species")
		
		# load data from file
		df = load_data()

		# prepare layout
		col1, col2 = st.columns([10, 1])

		# build the input form
		with col1.form("values_form"):
			search_value = st.text_input("Search query")
			is_submitted = st.form_submit_button("Search")
			# process submitted data
			if is_submitted:
				df = df[df['Compound name'].str.contains(search_value, regex=False, case=False)]

		# draw the table
		col1.dataframe(df)