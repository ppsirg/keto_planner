def get_ingredients(raw_text):
    """toma un texto y saca una lista de items y sus cantidades"""
    ingredients = []
    for l in raw_text.split('\n'):
        if len(l) > 1:
            ingredients.append(l.split(' '))
    return ingredients
