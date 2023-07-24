from decimal import Decimal


def calculate_tab(products):
    total_price = Decimal(0)
    for product in products:
        amount = product.get('amount')
        price = Decimal(product.get('price', 0))
        total_price = (total_price + price) * amount

    total_price_str = f"subtotal: ${total_price:.2f}"
    return {"subtotal": f"${total_price:.2f}"}
