import json


def write_order_to_json(json_name, item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    with open(json_name, 'r') as js:
        data = json.load(js)
    open(json_name, 'w').close()
    data['orders'] += [dict_to_json]
    with open(json_name, 'a') as js:
        json.dump(data, js, indent=4)

    with open(json_name) as js:
        print(js.read())


orders_dict = {'orders': []}
with open('order.json', 'w') as js:
    json.dump(orders_dict, js)
write_order_to_json('order.json', 'printer', '10', '6700', 'ivanov', 'today')
write_order_to_json('order.json', 'pc', '12', '226700', 'divanov', '21.11.22')
write_order_to_json('order.json', 'phone', '121', '96900', 'parov', '12.01.22')
