import calendar
import csv
import pandas as pd

from json2csv.read_json import ReadJson

class Writecsv:

    @classmethod
    def customers_info(cls):
        customers = []
        for c_data in ReadJson.json_date:
            customers_data = {
                "CustomerID": c_data['customer_id'],
                "First Name": c_data['customer_firstname'],
                "Last Name": c_data['customer_lastname'],
                "Customer Phone": c_data['billing_address']['telephone'],
                "Customer Email": c_data['customer_email']

            }
            customers.append(customers_data)
        #     with open('Customers.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
        #         w = csv.DictWriter(f, customers_data.keys())
        #         w.writeheader()
        #         w.writerow(customers_data)
        cls.dict2csv(dict_data=customers, file_name='Customers')

    @classmethod
    def customer_address(cls):
        c_address = []
        for c_data in ReadJson.json_date:
            street = c_data['billing_address']['street']
            address = {
                "CustomerID": c_data['customer_id'],
                "AddressID": c_data['billing_address_id'],
                "Address Type": c_data['billing_address']['address_type'],
                "Street Address": ' '.join(street),
                "City": c_data['billing_address']['city'],
                "Region": c_data['billing_address']['region'],
                "Country": c_data['billing_address']['country_id'],
                "Postcode": c_data['billing_address']['postcode']

            }
            c_address.append(address)
        cls.dict2csv(dict_data=c_address, file_name='Customer Address')

    @classmethod
    def customer_order_master(cls):
        c_order_master = []
        for c_data in ReadJson.json_date:
            order_master = {
                "OrderID": c_data['entity_id'],
                "CustomerID": c_data['customer_id'],
                "Order Date": c_data['created_at'],
                "Payment ID": cls.payment_id(data=c_data['extension_attributes']['payment_additional_info']),
                "Total Quantity": c_data['total_qty_ordered'],
                "Grand Total": c_data['grand_total'],
                "Total Paid": c_data['total_paid'],
                "Order Status": c_data['status']

            }
            c_order_master.append(order_master)
        cls.dict2csv(dict_data=c_order_master, file_name='Customer Order Master')

    @classmethod
    def customer_order_details(cls):
        c_ord_data = []
        for c_data in ReadJson.json_date:
            for ord_data in c_data['items']:
                order_details = {
                    "OrderID": ord_data['order_id'],
                    "Product ID": ord_data['product_id'],
                    "Product Type": ord_data['product_type'],
                    "SKU": ord_data['sku'],
                    "Product Price": ord_data['price'],
                    "Order Quantity": ord_data['qty_ordered'],
                    "Any Discount": "Y" if ord_data['discount_amount'] > 0 else "N",
                    "Price-Discount": ord_data['discount_amount']

                }
                c_ord_data.append(order_details)
        cls.dict2csv(dict_data=c_ord_data, file_name='Customer Order Details')

    @classmethod
    def payment_details(cls):
        c_payment = []
        for c_data in ReadJson.json_date:
            card_exp_month = c_data['payment']['cc_exp_month']
            card_exp_year = c_data['payment']['cc_exp_year']
            c_exp_month_year = cls.exp_month_year(month=card_exp_month, year=card_exp_year)
            payment_data = {
                "Payment ID": cls.payment_id(data=c_data['extension_attributes']['payment_additional_info']),
                "CustomerID": c_data['customer_id'],
                "Method of Payment": c_data['payment']['method'],
                "Amount Paid": c_data['payment']['amount_paid'],
                "Card Type": c_data['payment']['cc_type'],
                "Card last 4 Digits": c_data['payment']['cc_last4'],
                "Card Expiry Month Year": c_exp_month_year
            }
            c_payment.append(payment_data)
        cls.dict2csv(dict_data=c_payment, file_name='Payment Details')


    @classmethod
    def exp_month_year(cls, month, year):
        exp_month = calendar.month_name[int(month)]
        exp_year = year[2:]
        return exp_month+exp_year

    @classmethod
    def dict2csv(cls, dict_data, file_name):
        df = pd.DataFrame(dict_data)
        df.to_csv(file_name+'.csv')

    @classmethod
    def payment_id(cls,data):
        for pay_info in data:
            if pay_info['key'] == 'payment_id':
                return pay_info['value']

