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


def generate_id(products: list) -> int:
    if not products:
        return 1
    max_id = max(products, key=lambda x: x['_id'])['_id']
    return max_id + 1


def add_product(products: list, **new_product: dict) -> dict:
    _id = generate_id(products)
    new_product['_id'] = _id
    products.append(new_product)
    return new_product
