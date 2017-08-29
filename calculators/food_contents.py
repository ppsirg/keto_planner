import re
from copy import deepcopy
from simulation.food import proteins, carbs


def do_calculation(ingredients_list, food_contents_dict):
    ingredients = deepcopy(ingredients_list)
    adjusts = {}
    total_content = 0
    partial_contents = {}
    for i in ingredients:
        if 'g' in i[-1]:
            adjust_weight_index = float(i[-1].replace('g', '')) / 100
        else:
            adjust_weight_index = float(i[-1])
        adjusts[i[0]] = adjust_weight_index
    for i in adjusts:
        content = food_contents_dict[i] * adjusts[i]
        partial_contents[i] = content
        total_content += content
    return total_content, partial_contents


def calculate_proteins(ingedients_list):
    """calculate proteins in a list of things"""
    total_content, partial_contents = do_calculation(ingedients_list, proteins)
    print('partial proteins contents: {}'.format(partial_contents))
    return total_content


def calculate_carbs(ingedients_list):
    """calculate carbs in a list of things"""
    total_content, partial_contents = do_calculation(ingedients_list, carbs)
    print('partial carbs contents: {}'.format(partial_contents))
    return total_content
