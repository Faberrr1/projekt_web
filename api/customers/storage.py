from functools import lru_cache

from .schema import Customer, Order, Product

CustomerStorageType = dict[int, Customer]
OrdersStorageType = dict[int, Order]
ProductsStorageType = dict[int, Product]

CUSTOMERS: CustomerStorageType = {}
ORDERS: OrdersStorageType = {
    0: Order(
        customer_id=0,
        order_items=[0,1],
        order_id=0,
    ),
    1: Order(
        customer_id=1,
        order_items=[2,3],
        order_id=1,
    ),
}
PRODUCTS: ProductsStorageType = {
    0: Product(name="Suszarka", price=10.0, description="Suszy", id=0),
    1: Product(name="Lodówka", price=100.0, description="Mrozi", id=1),
    2: Product(name="Pralka", price=50.0, description="Pierze", id=2),
    3: Product(name="Zmywarka", price=70.0, description="Myje", id=3),
}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS


@lru_cache(maxsize=1)
def get_orders_storage() -> OrdersStorageType:
    return ORDERS


@lru_cache(maxsize=1)
def get_products_storage() -> ProductsStorageType:
    return PRODUCTS