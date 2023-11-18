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
    print(f"The orders are as follows {order_str}")


get_sales_data()