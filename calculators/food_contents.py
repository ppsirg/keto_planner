"""
does calculators for statistics and analysis related with food intake
"""

import re
from copy import deepcopy
from simulation.food import proteins, carbs, fats, calories, alcoholics


class daily_intake_calculator(object):
    """
    object that calculates various stats given a list of daily intake in
    dictionary format with key as name of food and its quantities in grams.
    can calculate:
    - carbs, fats, proteins, calories
    - keto proportions
    """

    def __init__(self, food_contents_dict):
        self.daily_intake = food_contents_dict
        self.carb_content = self.calculate_carbs()
        self.protein_content = self.calculate_proteins()
        self.alcohol_content = self.calculate_alcoholics()
        self.fat_content = self.calculate_fats()

    def normalized_pertentage(self, partial, total):
        """
        calculate a percentage with 3 decimal digits
        """
        return round(((partial / total) * 100), ndigits=3)

    def calculate_calories_proportions(self):
        """
        9 calories per gram of fat
        4 calories per gram of proteins
        4 calories per gram of carbs
        7 calories per gram of alcohol
        source: http://www.nutristrategy.com/nutrition/calories.htm
        """
        carbs_calories = self.carb_content * 4
        protein_calories = self.protein_content * 4
        fat_calories = self.fat_content * 9
        alcohol_calories = self.alcohol_content * 7
        total_calories = carbs_calories + protein_calories + fat_calories + alcohol_calories
        return {
            'total_calories': total_calories,
            'fat': (
                fat_calories,
                self.normalized_pertentage(fat_calories, total_calories)),
            'carbs': (
                carbs_calories,
                self.normalized_pertentage(carbs_calories, total_calories)),
            'protein': (
                protein_calories,
                self.normalized_pertentage(protein_calories, total_calories)),
            'alcohol': (
                alcohol_calories,
                self.normalized_pertentage(alcohol_calories, total_calories)),
        }

    def keto_analysis(self):
        """
        do keto analysis
        """
        # declare proportions bias
        # source: https://www.ruled.me/guide-keto-diet/
        protein_carbs_range = (4, 6)  # ideal: 5
        fat_range = (63, 77)  # ideal: 70
        # get calories proportions
        report = self.calculate_calories_proportions()
        proportion = report['protein'][1] / report['carbs'][1]
        # valorate carbs, fats and proteins
        if proportion <= protein_carbs_range[0]:
            # too much carbs
            carbs_analysis = '[planned_{}%][real_{:.2f}%]: high'
            protein_analysis = '[planned_{}%][real_{:.2f}%]: low'
        elif proportion >= protein_carbs_range[1]:
            # too many proteins
            carbs_analysis = '[planned_{}%][real_{:.2f}%]: low'
            protein_analysis = '[planned_{}%][real_{:.2f}%]: high'
        else:
            # proteins and carbs are ok
            carbs_analysis = '[planned_{}%][real_{:.2f}%]: ok'
            protein_analysis = '[planned_{}%][real_{:.2f}%]: ok'
        if report['fat'][1] <= fat_range[0]:
            # need more fat
            fat_analysis = '[planned_{}%][real_{:.2f}%]: low'
        elif report['fat'][1] >= fat_range[1]:
            # need less fat
            fat_analysis = '[planned_{}%][real_{:.2f}%]: high'
        else:
            # fat is ok
            fat_analysis = '[planned_{}%][real_{}%]: fat in the range'
        return {
            'carbs': carbs_analysis.format(5, report['carbs'][1]),
            'protein': protein_analysis.format(25, report['protein'][1]),
            'fat': fat_analysis.format(70, report['fat'][1])
        }

    def tdee_analysis(self):
        """
        do tdee analysis
        """
        # calculate calories
        # TODO: compare with tdee plan
        pass

    def do_calculation(self, food_contents_dict):
        """
        calculate total and partial contents of any statistics in daily_intake
        given a dictionary with it's contents per 100g
        """
        ingredients = deepcopy(self.daily_intake)
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

    def calculate_proteins(self):
        """calculate proteins in a list of things"""
        total_content, partial_contents = self.do_calculation(proteins)
        print('partial proteins contents: {}'.format(partial_contents))
        return total_content

    def calculate_carbs(self):
        """calculate carbs in a list of things"""
        total_content, partial_contents = self.do_calculation(carbs)
        print('partial carbs contents: {}'.format(partial_contents))
        return total_content

    def calculate_fats(self):
        """calculate fats in a list of things"""
        total_content, partial_contents = self.do_calculation(fats)
        print('partial fat contents: {}'.format(partial_contents))
        return total_content

    def calculate_alcoholics(self):
        """calculate alcohol in a list of things"""
        total_content, partial_contents = self.do_calculation(alcoholics)
        print('partial alcohol contents: {}'.format(partial_contents))
        return total_content
