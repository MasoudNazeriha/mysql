import streamlit as st
import mysql.connector
import pandas as pd

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host="127.0.0.1:3306",
        user="root",  # Replace with your MySQL username
        password="",  # Replace with your MySQL password
        database="railseir"  # Replace with your database name
    )
    cursor = connection.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM karami")  # Replace with your table name

    # Fetch data
    data = cursor.fetchall()

    # Convert data to pandas DataFrame
    df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])

    # Display DataFrame in Streamlit frame
    st.write(df)

except mysql.connector.Error as err:
    st.error(f"Error: {err}")
finally:
    # Close connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
