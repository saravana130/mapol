import json



class ReadJson:
    json_date = None
    CustomerID = None
    customers = None

    @classmethod
    def read_json(cls):
        with open('orders_data.json') as f:
            date = json.load(f)
            cls.json_date = date['items']
        return cls.json_date
