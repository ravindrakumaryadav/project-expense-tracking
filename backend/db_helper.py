# import connector package
from contextlib import contextmanager
import mysql.connector
import os
import sys

# from Python.Ch_14.MySQL_Python import db_helper
from logging_setup import setup_logger

logger = setup_logger('db_helper')
@contextmanager
def get_db_Cursor(commit=False):
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="expense_manager"
    )
# check connection status
    if conn.is_connected():
        print("Connected")
    else:
        print("Not connected")
    cursor = conn.cursor(dictionary=True)
    yield cursor
    if commit:
        conn.commit()

    cursor.close()
    conn.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for date called with {expense_date}")
    with get_db_Cursor() as cursor:
        cursor.execute("select * from expenses where expense_date=%s",(expense_date,))
        expenses=cursor.fetchall()
        return expenses


# fetch 3rd heighest expense amount
def fetch_expense_amount():
    with get_db_Cursor() as cursor:
        cursor.execute("select amount from expenses order by amount desc limit 1 offset 2;")
        expense_amount=cursor.fetchall()
        return expense_amount


# insert records
def insert_expense_records(expense_date, amount,category,notes):
    logger.info(f"Insert expenses with date: {expense_date},amount:{amount},category:{category},notes:{notes}")
    with get_db_Cursor(commit=True) as cursor:
        cursor.execute("insert into expenses (expense_date, amount,category,notes)"
                       "values(%s,%s,%s,%s)",(expense_date, amount,category,notes))



def delete_records(expense_date):
    logger.info(f"Expenses expenses for date called with {expense_date}")
    with get_db_Cursor(commit=True) as cursor:


        cursor.execute("delete from expenses where expense_date=%s",(expense_date,))


def fetch_expense_summary(start_date, end_date):
    logger.info(f"Fetch expenses summary between date:{start_date} and date: {end_date}")
    with get_db_Cursor() as cursor:
        # cursor.execute('SET SQL_SAFE_UPDATES = 0;')
        cursor.execute(""
                       '''
                            select category, sum(amount) as total
                            from expenses
                            where expense_date
                            between %s and %s
                            group by category
                         '''
                       , (start_date, end_date))
        data=cursor.fetchall()
        return data



if __name__ == '__main__':
   expenses=  fetch_expenses_for_date('2026-01-10')
   print(expenses)
   insert_expense_records('2026-01-10',40,'Coconut water','Healthy drinks' )
   insert_records=  fetch_expenses_for_date('2026-02-10')
   print(insert_records)
   delete_records('2026-01-10')
   insert_records = fetch_expenses_for_date('2026-02-10')
   delete_records('2026-01-10')
   delete_records('2026-01-10')
   print(insert_records)
   summary=fetch_expense_summary('2024-08-02','2024-08-03')
   for row in summary:
       print(row)
  # project_root=os.path.join(os.path.dirname(__file__),'..')
  # sys.path.insert(0,project_root)
  # print(sys.path)