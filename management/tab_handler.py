from menu import products


def calculate_tab(list):
    total_price = 0
    for item in list:
        for product in products:
            if product.get("_id") == item.get("_id"):
                total_price += item.get('amount') * product.get('price')

    return {"subtotal": f"${round(total_price, 2)}"}
