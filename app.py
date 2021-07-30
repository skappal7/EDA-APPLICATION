# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RmeREGP9-HCBerGfdaiObpR0spYOAFLx
"""

import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

"""![](https://skappal7.files.wordpress.com/2021/07/cropped-cropped-cropped-9datadojo-1.png)"""

# Web App Title
st.markdown('''
# **Exploratory Data Analysis Application**
This is the **EDA App** created in Streamlit using the **pandas-profiling** library.
**Credit:** App built in `Python` + `Streamlit` by [Sunil Kappal](https://www.datadojo.co.in))
---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/skappal7/Analytics-Maturity-App/main/Analytics%20Maturity%20Data.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)