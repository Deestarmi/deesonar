from app import calculate_discount, ShoppingCart

def test_discount():
    assert calculate_discount(100, 10) == 90

def test_cart_total():
    cart = ShoppingCart()
    cart.add_item("book", 200)
    cart.add_item("pen", 50)
    assert cart.total() == 250