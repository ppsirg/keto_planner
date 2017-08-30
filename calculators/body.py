"""
does calculators for statistics and analysis related with body measurements
"""

def calculate_bmi(weight, height):
    """calculate bmi given weight in kg and height in meters"""
    return weight / (height ^ 2)
