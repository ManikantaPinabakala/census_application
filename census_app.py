# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.set_option('deprecation.showPyplotGlobalUse', False)

# Add title on the main page and in the sidebar.
st.title('Census Application')
st.sidebar.title('Exploratory data analysis')
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox('Show raw data'):
  st.subheader('Original Dataset')
  st.dataframe(census_df)

st.sidebar.subheader('Visualization Selector')
plots = st.sidebar.multiselect('Select the Charts/Plots:', ('Pie Chart', 'BoxPlot', 'CountPlot'))

if 'Pie Chart' in plots:
	st.sidebar.subheader('Pie Chart')
	pie_cols = st.sidebar.multiselect('Select the column for Pie Chart:', ('Gender', 'Income'))
	for i in pie_cols:
		pie_data = census_df[i.lower()].value_counts()

		plt.figure(figsize = (15, 5), dpi = 96)
		st.subheader(f'Pie Chart for {i}:')
		plt.pie(pie_data, labels = pie_data.index, autopct = '%1.2f%%', startangle = 30, explode = [0.1]*len(pie_data.index))
		st.pyplot()

if 'BoxPlot' in plots:
	st.sidebar.subheader('BoxPlot')
	box_cols = st.sidebar.multiselect('Select the column to display the ranges of hours-per-week column for:', ('Gender', 'Income'))

	for i in box_cols:
		plt.figure(figsize = (15, 5), dpi = 96)
		st.subheader(f'BoxPlot for hours-per-week per each {i} group:')
		sns.boxplot(x = 'hours-per-week', y = i.lower(), data = census_df)
		st.pyplot()

if 'CountPlot' in plots:
	plt.figure(figsize = (15, 8), dpi = 96)
	st.subheader(f'CountPlot for workclass column based on income group')
	sns.countplot(x = 'workclass', hue = 'income', data = census_df)
	st.pyplot()











