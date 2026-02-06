import streamlit as st
from datetime import date
import requests as rq

API_URL="http://localhost:8000"


def add_update_tab():
    st.date_input(
            "Enter date",
            date(2024,8,2),
            label_visibility="collapsed",
            # changed
            key = "selected_date",

        #     -----
        )
    selected_date = st.session_state.selected_date
     # print(selected_date)

    response = rq.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
        # st.write(existing_expenses)
    else:
        st.error("Failed to get expense data")
        existing_expenses = []


    #  categories
    categories=[
             "Entertainment",
             "Shopping",
             "Food",
            "Rent",
            "Pani Puri",
            "Other",
            "Icecream"
            ]
    # FORM KEY CHANGES WITH DATE
    form_key = f"expense_form_{selected_date}"

    #Form detail --- starts from here... (form key changed from - "key- expense_form")
    with st.form(key=form_key):


        col1, col2, col3 = st.columns(3)
        with col1:
            col1.subheader("Amount")
        with col2:
            col2.subheader("Category")
        with col3:
            col3.subheader("Notes")
        expenses=[]
        for row in range(5):
            if row<len(existing_expenses):
                amount=existing_expenses[row]['amount']
                category=existing_expenses[row]['category']
                notes=existing_expenses[row]['notes']
            else:
                amount=0.0
                category="Rent"
                notes=""


            col1,col2,col3=st.columns(3)
            with col1:
                amount_input = st.number_input(
                        label="Amount",
                        min_value=0.0,
                        step=1.0,
                        value=amount,
                        # key must have pass row as well as date
                        key=f"amount_{row}_{selected_date}",
                        label_visibility="collapsed"
                    )
            with col2:
                category_input = st.selectbox(
                        label="Category",
                        options=categories,
                        index=categories.index(category),
                        # key must have pass row as well as date
                        key=f"category_{row}_{selected_date}",
                        label_visibility="collapsed"
                )
            with col3:
                notes_input = st.text_input(
                        label="Notes",
                        value=notes,
                        # key must have pass row as well as date
                        key=f"notes_{row}_{selected_date}",
                        label_visibility="collapsed"
                    )
        expenses.append({
            "amount":amount_input,
            "category":category_input,
            "notes":notes_input
        })
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            filtered_expenses=[expense for expense in expenses if expense["amount"]>0]
            response=rq.post(f"{API_URL}/expenses/{selected_date}",json=filtered_expenses)
        if response.status_code == 200:
            st.success("Successfully submitted")
        else:
            st.error("Failed to submit")