# WhatsApp Message Bot

This Streamlit app allows you to send WhatsApp messages to multiple contacts by extracting phone numbers from an Excel file. You can customize the message and manage the contacts' numbers, including adding a country code if it's not already present in the data.

## Features

- **Upload Excel File**: Upload an Excel file containing contact numbers.
- **Specify Column Name**: Indicate the column that contains the phone numbers.
- **Custom Message**: Enter the message you want to send to all contacts.
- **Country Code Handling**: Option to specify a country code if it's not included in the numbers.
- **Automated Messaging**: Send messages instantly to all valid numbers in the list.

## Requirements

- Python 3.x
- pandas
- pywhatkit
- streamlit
- openpyxl (for reading Excel files)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Jibin-Gigi/Whatsapp-Message-Bot.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Whatsapp-Message-Bot
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Upload your Excel file:** The file should contain a column with phone numbers.

3. **Specify the column name:** Enter the name of the column containing the phone numbers.

4. **Enter your message:** Type the message you want to send to the contacts.

5. **Country code options:** Indicate whether the numbers in your file include a country code. If not, provide the country code.

6. **Send messages:** Click the "Send" button to start sending messages.

## Important Notes

- Ensure that the phone numbers in your Excel file are formatted correctly and include country codes if required.
- The `pywhatkit.sendwhatmsg_instantly` function requires that WhatsApp Web is open and logged in on your browser. This tool automates the messaging process but cannot bypass WhatsApp's security and privacy measures.
- Use this tool responsibly and ensure you have consent from the contacts to send them messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/) for the web interface.
- [pywhatkit](https://github.com/Ankit404butfound/PyWhatKit) for the WhatsApp messaging functionality.
- [pandas](https://pandas.pydata.org/) for data manipulation.

## Contributing

Feel free to fork this project and make contributions. Pull requests are welcome!
