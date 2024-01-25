import streamlit as st
import pandas as pd

st.title('Customer Info')

df1=pd.read_csv('HHC_Data.csv')

col1,col2,col3=st.columns(3)

customer_id = col1.text_input("Enter customer id")
connection_number = col2.text_input("Enter connection number")
customer_name= col3.text_input("Enter the customer name")
municipality = col1.selectbox("Enter the municipality",['Kathmandu','Lalitpur'])
areas_list = df1['Areas'].dropna().unique().tolist()

if municipality=='Kathmandu':
    Area= col2.selectbox("select the Areas",areas_list)
    ward = col3.selectbox("select the ward",[i for i in range(1,33)])

if municipality=='Lalitpur':
    Area= col2.selectbox("select the Areas",areas_list)
    ward = col3.selectbox("select the ward",[i for i in range(1,30)])

contact_number = col1.text_input("Enter the contact number")
phone_number = col2.text_input("Enter the alternative phone number")
Landmark = col3.text_input("Enter the Landmark")

if st.button("Generate Report"):
    # Process data and generate report
    report = f"Customer ID: {customer_id}\nConnection Number: {connection_number}\nCustomer Name: {customer_name}\n"
    report += f"Municipality: {municipality}\nArea: {Area}\nWard: {ward}\n"
    report += f"Contact Number: {contact_number}\nAlternative Phone Number: {phone_number}\nLandmark: {Landmark}"

    # Display the report
    st.text("Generated Report:")
    st.text(report)

    # Download button for the report
    st.download_button(
        label="Download Report",
        data=report,
        file_name=f"{customer_id}_report.txt",
        key="download_button"
    )