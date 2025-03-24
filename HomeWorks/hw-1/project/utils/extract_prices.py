def extract_prices(products):
    prices = []
    for item in products:
        prices.append(item.get_price())
    return prices
