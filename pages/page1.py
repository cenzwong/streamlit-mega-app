from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import api.myai21 as myai21
# import pyperclip

st.set_page_config(page_title="Plotting Demo", page_icon="📈")
"""
# NLP AI21Lab App
"""

with st.form("my_form"):
    result_json = {}
    key = st.text_input('Bring your own API Keys', 'jc5dvUcu1UVpWxqMcBCEUUUpFyVUrkvvvv')
    txtParaphrase = st.text_input('Paraphrase', '')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:

        result = myai21.ai21_rewrite(txtParaphrase, "general", key)
        print(result)
        
        result_list = result
        
        for resp in result_list:
            st.code(resp, language="ignore")