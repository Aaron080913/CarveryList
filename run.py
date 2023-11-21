import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Carvery_List')


def get_sales_data():
    """
    Get sales input from the user
    """
    print("Please enter carveries ordered from the last Sunday.")
    print("Data should be six numbers, seperated by commas.")
    print("Example: 5,10,15,20,25,30\n")
    order_str = input("Enter your orders here:")
    sales_data = order_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    converts all strings into integers.
    shows valueerror if string cannot be
    converted into an integer, or if not 6 number.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly six values required, you provided {len(values)}"
            )  
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()