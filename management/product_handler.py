from menu import products


def get_product_by_id(product_id):
    for product in products:
        if product['_id'] == product_id:
            return product
    return {}


def get_products_by_type(product_type):
    products_type = [product for product in products
                     if product['type'] == product_type]
    return products_type
