"""
different kind of clients for user to use calculators and see it's results
"""
import os
import argparse
from copy import deepcopy
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
    keto_analysis = calculator.keto_analysis()
    print(keto_analysis) # TODO: put display in test
    return carbs, proteins


class cmd_daily_keto_report(object):

    def __init__(self):
        # commandline parser
        self.p = argparse.ArgumentParser(
        prog='keto_planner commandline client',
        description='shows keto analysis given a path to csv consumption'
        )
        self.p.add_argument(
            'path',
            nargs=1,
            help='absolute path of a file with food list',
            type=str
        )
        # templates directory
        self.template_path = os.path.join(os.path.dirname(__file__), 'templates')

    def get_cmd_arguments(self):
        args = self.p.parse_args()
        return args.path[0]

    def get_intake_info(self):
        # get arguments
        path = self.get_cmd_arguments()
        # get intake information
        with open(os.path.join(os.getcwd(), path), 'r') as f:
            raw_text = f.read()
        return get_ingredients(raw_text)

    def main(self):
        food_list = self.get_intake_info()
        calculator = daily_intake_calculator(food_list)
        # calculate calories
        calories_report = calculator.calculate_calories_proportions()
        # calculate keto analysis
        keto_report = calculator.keto_analysis()
        # show report
        print('total calories: {}'.format(calories_report['total_calories']))
        print('\nketo_analysis:')
        for i in keto_report:
            print('[{}]: {}'.format(i, keto_report[i]))

class complete_report(cmd_daily_keto_report):

    def __init__(self):
        super().__init__()

    def calculate_detail(self, partial_contents):
        """calculates a list with ordered partial contents"""
        contents = deepcopy(partial_contents)
        total = 0
        for n in contents.values():
            total += n
        contents_list = [
            (a, contents.get(a))
            for a in sorted(contents, key=contents.__getitem__, reverse=True)
            ]
        result = [
            {'name': a, 'cals': b, 'per': (b / total) * 100}
            for a, b in contents_list
            ]
        return result

    def main(self):
        food_list = self.get_intake_info()
        calculator = daily_intake_calculator(food_list)
        # get food stats
        calories = calculator.calculate_calories_proportions()
        fats = calculator.calculate_fats()
        proteins = calculator.calculate_proteins()
        carbs = calculator.calculate_carbs()
        # print(calories)
        # print(fats)
        # print(proteins)
        # print(carbs)
        data = {
            'total_calories': calories['total_calories'],
            'fat': {
                'cal': calories['fat'][0],
                'per': calories['fat'][1],
                'g': fats['total'],
                'status': 'not_implemented', # TODO: implement this
                'ideal': 70,
                'detail': self.calculate_detail(fats['partial'])
                },
            'protein': {
                'cal': calories['protein'][0],
                'per': calories['protein'][1],
                'g': proteins['total'],
                'status': 'not_implemented', # TODO: implement this
                'ideal': 25,
                'detail': self.calculate_detail(proteins['partial'])
                },
            'carbs': {
                'cal': calories['carbs'][0],
                'per': calories['carbs'][1],
                'g': carbs['total'],
                'status': 'not_implemented', # TODO: implement this
                'ideal': 5,
                'detail': self.calculate_detail(carbs['partial'])
                },
            'carbs_protein_ideal': 5,
            'carbs_protein_ratio': proteins['total'] / carbs['total'],
            'carbs_protein_advice': 'not_implemented' # TODO: implement this
        }
        # load template
        template_path = os.path.join(
            self.template_path,
            'complete_commandline_report.txt'
            )
        with open(template_path, 'r') as f:
            template = f.read()
        print(template.format(**data))
