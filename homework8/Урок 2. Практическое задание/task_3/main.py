import yaml
from yaml.loader import SafeLoader

data_dict = {"items": ['computer', 'phone', 'table', 'keyboard'],
             'items-quantity': 100, "items-price":
                 {'computer': '20000 U+20AC', 'phone': '400 U+20AC', 'table':
                     '50 U+20AC', 'keyboard': '100 U+20AC'}}
with open('data.yaml', 'w') as out:
    yaml.dump(data_dict, out, default_flow_style=False, allow_unicode=True)

with open('data.yaml', 'r') as out:
    in_data = yaml.load(out, Loader=SafeLoader)
print(in_data)
