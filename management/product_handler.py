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


def menu_report():
    if not products:
        return "No products found"
    total_products = len(products)
    total_price = sum(product["price"] for product in products)
    average_price = total_price / total_products

    product_types = {}
    for product in products:
        product_type = product["type"]
        product_types[product_type] = product_types.get(product_type, 0) + 1

        most_common_type = max(product_types, key=product_types.get)

        report_string = f""
        report_string = f"Products Count: {total_products} - "
        report_string += f"Average Price: ${average_price:.1f} - "
        report_string += f"Most Common Type: {most_common_type}"

        return report_string


def get_product_by_id(_id):
    if not isinstance(products, list):
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == _id:
            return product
    raise TypeError("product id must be an int")


def get_products_by_type(type):
    if not isinstance(products, str):
        raise TypeError("product type must be a str")
    for product in products:
        if product["type"] == type:
            return product
    raise TypeError("product type must be a str")
