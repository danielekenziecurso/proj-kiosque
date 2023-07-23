from management.product_handler import *
from management.tab_handler import *
from menu import products


if __name__ == "__main__":
    # print(get_product_by_id(1))
    # print(get_products_by_type('fruit'))
    # new_product = {
    #     "title": "Bolinho JS",
    #     "price": 1.0,
    #     "rating": 2,
    #     "description": "Bolinho de JS com cenoura",
    #     "type": "bakery",
    # }

    # result = add_product(products, new_product)
    # print(result)

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]

    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))

    print(calculate_tab(table_2))
