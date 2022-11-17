import streamlit as st
import plotly.graph_objects as go 



#-------------settings---------------
incomes = ["1","2","3"]
expenses = ["1","2","3"]
currency = "THB"
Page_tittle = "Income and Expense tracker"
page_itcon = ":money_with_wings:"
layout = "centered"
#------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout,layout)
st.title(page_title + " " + page_icon)
