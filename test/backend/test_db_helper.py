from backend import db_helper
import datetime
import pytest
import os
import sys



# print(__file__)

def test_fetch_expenses_for_date():
    expenses=db_helper.fetch_expenses_for_date("2024-08-02")
    assert len(expenses)==6
    # assert expenses[0]["expense_date"]==datetime.date(2024, 8, 2)
    assert expenses[0]["amount"]==50
    assert expenses[0]["category"]=="Entertainment"
