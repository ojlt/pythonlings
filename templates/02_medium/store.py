"""
Store with Products and Offers

Assume that you have a Store selling many Products. Some Products can
optionally be attached to at most one offer, for example a Buy N Get 1 Free
Offer (BuyNGet1FreeOffer) or a Percentage Reduction Offer
(PercentageReductionOffer). These offers are applied per Product at checkout.

Task 1:
Complete the init_from_json(json_filename) method of the Store class to
populate Store's products attribute (a dict) with instances of Products read
from the JSON file given by json_filename, indexed by the product ID.

The JSON gives a list of products, where each product has the keys "id",
"name" and "price". Some products also have an "offer" key, indicating that
there is an offer associated with the product. This could either be "bnf1"
(BuyNGet1FreeOffer) or "percent" (PercentageReductionOffer), with "n" giving
the values of the offer.

Task 2:
Complete the calculate_total(cost_per_item, quantity) method of both
PercentageReductionOffer and BuyNGet1FreeOffer classes. These methods should
return the total price given the cost of a single product and the quantity,
after applying the offer.

For PercentageReductionOffer, this should be the full cost reduced by the
specified percentage.

For BuyNGet1FreeOffer, this should be the cost after deducting the free
products. For example, for a product with a cost_per_item of 1.00, for a
Buy 2 Get 1 Free offer:
- a quantity of 3 should return 2.00 (price of 2 items since 1 is free)
- a quantity of 6 should return 4.00 (price of 4 items with 2 free items)
"""

# I AM NOT DONE


class Store:
    def __init__(self):
        self.products = {}

    def init_from_json(self, json_filename):
        # TODO: Complete
        pass


class Product:
    def __init__(self, id_, name, price, offer=None):
        self.id = id_
        self.name = name
        self.price = price
        if offer is None:
            self.offer = NoOffer()
        else:
            self.offer = offer

    def __repr__(self):
        return f"<{self.id}: {self.name} (${self.price}) {self.offer}>"

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.price == other.price
            and self.offer == other.offer
        )

    def calculate_price(self, quantity):
        return self.offer.calculate_total(self.price, quantity)


class NoOffer:
    def __init__(self):
        pass

    def __repr__(self):
        return "(No offer)"

    def __eq__(self, other):
        return isinstance(other, NoOffer)

    def calculate_total(self, cost_per_item, quantity=1):
        return cost_per_item * quantity


class PercentageReductionOffer:
    def __init__(self, percent_discount=0.0):
        self.percent_discount = percent_discount

    def __repr__(self):
        return f"({self.percent_discount * 100}% off)"

    def __eq__(self, other):
        return (
            isinstance(other, PercentageReductionOffer)
            and self.percent_discount == other.percent_discount
        )

    def calculate_total(self, cost_per_item, quantity=1):
        # TODO: Complete
        pass


class BuyNGet1FreeOffer:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"(Buy {self.n} Get 1 Free Offer)"

    def __eq__(self, other):
        return isinstance(other, BuyNGet1FreeOffer) and self.n == other.n

    def calculate_total(self, cost_per_item, quantity=1):
        # TODO: Complete
        pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
import json
import os


def is_close(x, y, eps=0.0000001):
    return abs(y - x) < eps


def setup_test_file():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(test_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    products = [
        {"id": "1000", "name": "apple", "price": 0.75, "offer": {"type": "bnf1", "n": 3}},
        {"id": "2000", "name": "banana", "price": 1.00, "offer": {"type": "percent", "n": 0.25}},
        {"id": "1200", "name": "pear", "price": 0.85}
    ]

    products_file = os.path.join(data_dir, "products.json")
    with open(products_file, "w") as f:
        json.dump(products, f)

    return products_file


def test_percent_offer():
    offer = PercentageReductionOffer(0.5)
    total = offer.calculate_total(1.2, 15)
    assert is_close(total, 9)

    offer = PercentageReductionOffer(0.25)
    total = offer.calculate_total(1.2, 15)
    assert is_close(total, 13.5)


def test_buy_n_get_1_free_offer():
    n = 2
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(1.0, 3)
    assert is_close(total, 2.0)

    n = 2
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(0.5, 15)
    assert is_close(total, 5)

    n = 3
    offer = BuyNGet1FreeOffer(n)
    total = offer.calculate_total(2.0, 4)
    assert is_close(total, 6.0)


def test_init_from_json():
    products_file = setup_test_file()
    store = Store()
    store.init_from_json(products_file)

    expected_values = {
        "1000": Product("1000", "apple", 0.75, BuyNGet1FreeOffer(3)),
        "2000": Product("2000", "banana", 1.00, PercentageReductionOffer(0.25)),
        "1200": Product("1200", "pear", 0.85, NoOffer()),
    }

    assert store.products == expected_values


if __name__ == "__main__":
    test_percent_offer()
    test_buy_n_get_1_free_offer()
    test_init_from_json()
    print("All tests passed!")
