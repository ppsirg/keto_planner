"""contents of substances per unit or per 100g"""
import os


def load_csv_food_data(path):
    """
    load google-obtained data from a csv file
    """
    food_name = []
    carbs = []
    proteins = []
    fats = []
    alcoholics = []
    calories = []
    with open(path, 'r') as csv_file:
        for line in csv_file:
            fd, cr, pr, ft, al, cl = line.strip().split(' ')
            food_name.append(fd)
            carbs.append(float(cr))
            proteins.append(float(pr))
            fats.append(float(ft))
            alcoholics.append(float(al))
            calories.append(float(cl))
    return (
        dict(zip(food_name, carbs)),
        dict(zip(food_name, proteins)),
        dict(zip(food_name, fats)),
        dict(zip(food_name, alcoholics)),
        dict(zip(food_name, calories))
        )


carbs, proteins, fats, alcoholics, calories = load_csv_food_data(
    os.path.join(os.path.dirname(__file__), 'food.csv')
)


# for local testing
if __name__ == '__main__':
    response = load_csv_food_data(
        os.path.join(os.path.dirname(__file__), 'food.csv')
        )
    print(response)


# previous dictionary-approach

# proteins = {
#     'huevos': 6.3,
#     'aguacate': 4,
#     'espinaca': 5.3,
#     'mani': 34,
#     'queso': 14.2,
#     'brocoli':2.8,
#     'pollo': 27,
#     'mayo': 1,
# }
#
# carbs = {
#     'huevos': 4.2,
#     'aguacate': 4,
#     'espinaca': 2.4,
#     'mani': 7,
#     'queso': 1.6,
#     'brocoli': 4,
#     'pollo': 1,
#     'mayo': 1,
# }
