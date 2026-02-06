import streamlit as st
import pandas as pd

st.title('Expense Tracking System')
st.header('Streamlit Core Feature')
st.subheader('Subheader text element')
st.text("This is a simple text element")

#  data display
st.subheader('Data Display')
st.write("write text on the webpages")
df=pd.DataFrame({
        "Date":['2026-01-08','2026-01-17','2026-01-06','2026-01-05'],
        "Amount":[10,20,30,40],
        })
st.table(df)
st.table({'column 1':[1,2,3],'column 2':[2,1,3]})


#
st.subheader('Charts')
st.line_chart([1,2,3,4])
expense_dt=st.date_input('Expense Date: ')

#user input
st.subheader('Data Display')
value=st.slider("Select a value",0,100)
st.write(f"Selected value is: {value}")


# Checkbox
if st.checkbox("Show/Hide"):
    st.write("Check box is checked")
else:
    st.write("Check box is unchecked")


# select box
option =st.selectbox("Select a number",[1,2,3,4])
st.write(f"Selected number is: {option}")

# multiselect
option=st.multiselect("Select a number",[1,2,3,4])
st.write(f"Selected number is: {option}")


if expense_dt:
    st.write(f"Fetching expenses for {expense_dt}")