import pytest

# Import the functions to be tested
from project import is_high_fodmap_dish, get_direct_match, get_closest_match

# Sample data for testing
fodmap_dict = [
    {"name": "garlic", "fodmap": "high"},
    {"name": "onion", "fodmap": "high"},
    {"name": "carrot", "fodmap": "low"},
    {"name": "spinach", "fodmap": "low"}
]

dish_high_fodmap = {
    "Dish": "Garlic Chicken",
    "Main Ingredients": "chicken; garlic",
    "Seasoning": "salt, pepper"
}

dish_low_fodmap = {
    "Dish": "Carrot Salad",
    "Main Ingredients": "carrot; spinach",
    "Seasoning": "olive oil, lemon juice"
}


# Test for is_high_fodmap_dish function
def test_is_high_fodmap_dish():
    assert is_high_fodmap_dish(dish_high_fodmap, fodmap_dict) is True, "Dish with high FODMAP ingredients should return True"
    assert is_high_fodmap_dish(dish_low_fodmap, fodmap_dict) is False, "Dish with low FODMAP ingredients should return False"


# Test for get_direct_match function
def test_get_direct_match():
    assert get_direct_match("garlic", fodmap_dict) == "garlic", "Function should return the exact match for 'garlic'"
    assert get_direct_match("onion", fodmap_dict) == "onion", "Function should return the exact match for 'onion'"
    assert get_direct_match("potato", fodmap_dict) is None, "Function should return None for an unmatched ingredient"


# Test for get_closest_match function
def test_get_closest_match():
    assert get_closest_match("carrot", fodmap_dict) == "carrot", "Function should return 'carrot' as the closest match"
    assert get_closest_match("spin", fodmap_dict) == "spinach", "Function should return 'spinach' as the closest match for partial keyword 'spin'"
    assert get_closest_match("tomato", fodmap_dict) == "tomato not found", "Function should return 'not found' for unmatched keyword 'tomato'"


# Run tests
if __name__ == "__main__":
    pytest.main()
