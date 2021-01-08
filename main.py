import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.title('csv profiler')

csv_file = st.file_uploader(label='CSV file to profile', type='csv')
separator = st.selectbox('Seperator type', [';', ','])

if csv_file is not None:
    data = pd.read_csv(csv_file, error_bad_lines=False, sep=separator)
    pr = ProfileReport(data, explorative=True)

    st_profile_report(pr)