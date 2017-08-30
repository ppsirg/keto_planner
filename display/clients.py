"""
different kind of clients for user to use calculators and see it's results
"""

from processing.parsers import get_ingredients
from calculators.food_contents import daily_intake_calculator


def full_food_calculator(file_path):
    # get text from file_path
    with open(file_path, 'r') as f:
        raw_text = f.read()
    # get data from text
    food_list = get_ingredients(raw_text)
    calculator = daily_intake_calculator(food_list)
    # do calculations of proteins
    proteins = calculator.calculate_proteins()
    # do calculations of carbs
    carbs = calculator.calculate_carbs()
    # report of calories proportion
    report = calculator.calculate_calories_proportions()
    print(report) # TODO: put display in test
    return carbs, proteins
