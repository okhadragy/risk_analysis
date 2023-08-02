import streamlit as st
import os
st.set_page_config(page_title="Home",layout="wide")


# embed streamlit docs in a streamlit app
st.title("File Upload")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    # Return the processed result if needed
    st.write("Processing complete!")