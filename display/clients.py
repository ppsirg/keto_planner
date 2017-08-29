from processing.parsers import get_ingredients
from calculators.food_contents import calculate_proteins, calculate_carbs


def full_food_calculator(file_path):
    # get text from file_path
    with open(file_path, 'r') as f:
        raw_text = f.read()
    # get data from text
    food_list = get_ingredients(raw_text)
    # do calculations of proteins
    proteins = calculate_proteins(food_list)
    # do calculations of carbs
    carbs = calculate_carbs(food_list)
    return carbs, proteins
