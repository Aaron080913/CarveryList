import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter which roast you would like.")
        print("Data should be seven numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60,70\n")

        order_str = input("Enter your data here: ")

        sales_data = order_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 7 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def worksheet_update(data, worksheet):
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet has been successfully updated\n")


def calculate_surplus_data(sales_row):
    """
    Compares sales with the stock list to alter the surplus.

    The Surplus indicates-
    positive = Waste
    Negative = extra made
    """

    print("Calculating Surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def get_last_5_Sunday_sales():
    """
    collects the last 5 sundays worth of data and returns this as a list.
    """
    sales = SHEET.worksheet("sales")

    columns = []
    for ind in range(1, 8):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    return columns


def calculate_stock_data(data):
    """
    Calculates the average stock for each roast & adds 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / 5
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data
    

def main():
    """
    Run Program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    worksheet_update(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    worksheet_update(new_surplus_data, "surplus")
    sales_columns = get_last_5_Sunday_sales()
    stock_data = calculate_stock_data(sales_columns)
    worksheet_update(stock_data, "stock")


print("Sunday Carvery Roast Ordering Station")
main()
