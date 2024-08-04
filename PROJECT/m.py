import streamlit as st
import pandas as pd
import mysql.connector

# Establish a MySQL connection
def create_conn():
    conn = mysql.connector.connect(
        user='root',
        password='Abhinavbansal@123',
        host='localhost',
        database='hims'
    )
    return conn

# Fetch data from the database
def fetch_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hims.Doctors")
    rows = cursor.fetchall()
    return rows

# Main function
def main():
    st.title("Hospital Information Management System")

    conn = create_conn()

    if st.button("Fetch Patient Data"):
        data = fetch_data(conn)
        df = pd.DataFrame(data, columns=['Doc_id', 'First_name', 'Last_name', 'Address', 'Phone No.'])
        st.dataframe(df)

    conn.close()

if __name__ == "__main__":
    main()
