from json2csv.read_json import ReadJson
from json2csv.write_csv import Writecsv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    ReadJson.read_json()
    Writecsv.customers_info()
    Writecsv.customer_address()
    Writecsv.customer_order_details()
    Writecsv.customer_order_master()
    Writecsv.payment_details()
if __name__ == '__main__':
    print_hi('mapol')

