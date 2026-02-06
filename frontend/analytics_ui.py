import streamlit as st
# from datetime import date
import requests as rq
from datetime import datetime
import pandas as pd


API_URL="http://localhost:8000"

def analytics_tab():
    col1,col2=st.columns(2)
    with col1:
        start_time = st.date_input("Start Date", datetime(2024,8,2))

    with col2:
        end_time = st.date_input("End Date", datetime(2024,8,3))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_time.strftime("%Y-%m-%d"),
            "end_date": end_time.strftime("%Y-%m-%d"),
        }
        response = rq.post(f"{API_URL}/analytics/",json=payload)
        response = response.json()

        data={
            "Category":list(response.keys()),
            "Total":[response[category]["total"] for category in response],
            "Percentage":[response[category]["percentage"] for category in response],
        }

        df=pd.DataFrame(data)
        df_sorted=df.sort_values(by=["Total"],ascending=False)

        st.table(df_sorted)
        st.title("Expense Breakdown by Category")
        st.bar_chart(
            data=df_sorted.set_index("Category")["Percentage"],
            width=800,
            height=400,
            use_container_width=True
        )

        # st.write(response)