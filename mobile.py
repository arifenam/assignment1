mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#print(mobile_data.get('data')[0].get('price').removesuffix(' USD'))
#ex : Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
#  Your Code Starts from here

# exh_rate = (mobile_data.get("exchnage_rate"))
i = 0

while i<len(mobile_data.get('data')):
    model= (mobile_data.get('data')[i].get('name'))
    country= (mobile_data.get('data')[i].get('made'))
    price = float(mobile_data.get('data')[i].get('price').removesuffix(' USD'))
    sent1 = f'{model} is made in {country}'
    sent2 =f'The price is {price} USD which is almost equal to {round(price * (mobile_data.get("exchnage_rate")))}'
    i += 1
    print(sent1,sent2)

