from .ingredients import INGREDIENTS

def calculate_recipe(recipe):
    total_calories = 0
    total_cost = 0
    for ingredient, quantity in recipe.items():
        ingredient_info = INGREDIENTS[ingredient]
        total_calories += ingredient_info['калории'] * (quantity / 100)
        total_cost += ingredient_info['цена'] * (quantity / 100)
    return total_calories, total_cost