import streamlit as st
import pandas as pd
import os
from PIL import Image

st.title('Customer Info')

# Load existing data from CSV (if any)
csv_file_path = 'customer_data.csv'
if os.path.exists(csv_file_path):
    existing_data = pd.read_csv(csv_file_path)
else:
    existing_data = pd.DataFrame(columns=['Customer ID', 'Connection Number', 'Customer Name', 'Municipality', 'Area', 'Ward', 'Contact Number', 'Alternative Phone Number', 'Landmark', 'Image Path'])

df1 = pd.read_csv('HHC_Data.csv')

col1, col2, col3 = st.columns(3)


customer_id = col1.text_input("Enter customer id")
connection_number = col2.text_input("Enter connection number")
customer_name = col3.text_input("Enter the customer name")
municipality = col1.selectbox("Enter the municipality", ['Kathmandu', 'Lalitpur'])
areas_list = df1['Areas'].dropna().unique().tolist()

if municipality == 'Kathmandu':
    Area = col2.selectbox("Select the Areas", areas_list)
    ward = col3.selectbox("Select the ward", [i for i in range(1, 33)])

if municipality == 'Lalitpur':
    Area = col2.selectbox("Select the Areas", areas_list)
    ward = col3.selectbox("Select the ward", [i for i in range(1, 30)])

contact_number = col1.text_input("Enter the contact number")
phone_number = col2.text_input("Enter the alternative phone number")
Landmark = col3.text_input("Enter the Landmark")

if st.button("Add customer data"):
    # Process data and generate report
    report = f"Customer ID: {customer_id}\nConnection Number: {connection_number}\nCustomer Name: {customer_name}\n"
    report += f"Municipality: {municipality}\nArea: {Area}\nWard: {ward}\n"
    report += f"Contact Number: {contact_number}\nAlternative Phone Number: {phone_number}\nLandmark: {Landmark}"

    # Append the new data to the existing data
    new_entry = pd.DataFrame({'Customer ID': [customer_id],
                              'Connection Number': [connection_number],
                              'Customer Name': [customer_name],
                              'Municipality': [municipality],
                              'Area': [Area],
                              'Ward': [ward],
                              'Contact Number': [contact_number],
                              'Alternative Phone Number': [phone_number],
                              'Landmark': [Landmark]})

    updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

    # Save the updated data to CSV
    updated_data.to_csv('customer_data.csv', index=False)

    st.text("Generated Report:")
    st.text(report)
