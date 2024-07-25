import pandas as pd
import pywhatkit as kit
import time
import streamlit as st

def messager_bot(uploaded_file, column_name, country_code, message):
    try:
        # Load the Excel file
        data = pd.read_excel(uploaded_file)

        # Check if the column name exists
        if column_name not in data.columns:
            st.error(f"Column '{column_name}' not found in the Excel sheet.")
            return

        # Convert to string and drop NaN values
        numbers = data[column_name].dropna().astype(str)

        for number in numbers:
            number = number.strip()
            if not number.startswith('+'):
                number = f"{country_code}{number}"
            
            try:
                # Send WhatsApp message
                kit.sendwhatmsg_instantly(f"{number}", message, 15, True, 2)
                st.write(f"Message sent to {number}")
                time.sleep(5)
            except Exception as e:
                st.write(f"Failed to send message to +{number}: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title('WhatsApp Message Bot')
    st.text('This app extracts contact numbers from an Excel file and sends a given message to the contacts.')

    uploaded_file = st.file_uploader('Choose your file with contacts (Excel format).')
    if uploaded_file:
        column_name = st.text_input('Enter the column name containing the phone numbers:')
        message = st.text_area('Enter the message you want to send:')

        has_country_code = st.radio('Does your file have country codes with numbers?', ['Yes', 'No'])
            
        country_code = ""
        if has_country_code == 'No':
            country_code = st.text_input('Enter your country code (e.g., +91 for India):')
            
        if st.button('Send'):
            if not column_name or not message:
                st.error('Please fill in all the required details.')
            elif has_country_code == 'No' and not country_code:
                st.error('Please enter the country code.')
            else:
                messager_bot(uploaded_file, column_name, country_code, message)

if __name__ == "__main__":
    main()
