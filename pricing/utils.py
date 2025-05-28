def calculate_price(service_type, complexity_level=1):
    base_prices = {
        'design': 5000,
        'ads': 7000,
        'seo': 6000,
    }
    return base_prices.get(service_type, 0) * complexity_level