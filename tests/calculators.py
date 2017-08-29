from unittest import TestCase, skip
from display.clients import full_food_calculator


class calculators_tests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculator(self):
        carbs, proteins = full_food_calculator("today.md")
        print('carbs: {}\nproteins: {}'.format(carbs, proteins))
