import csv
import json
import spacy
import inflect
import random
import datetime
import argparse


def determine_meal_time():
    """
    Determine the current meal time based on the hour.
    """
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 14:
        return 'Lunch'
    else:
        return 'Dinner'


def is_high_fodmap_dish(dish, fodmap_dict):
    """
    Check if a dish contains high FODMAP ingredients.
    """
    main_ingredients = []
    for ing in dish['Main Ingredients'].split(';'):
        main_ingredients.append(ing.strip().split(' [')[0].lower())
    print(f"\nChosen Dish Name: {dish['Dish']}\n\tmain_ingredients={main_ingredients!r}")

    direct_matches = []
    for ingredient in main_ingredients:
        ingredient_s = get_singular(ingredient)
        direct_match = get_direct_match(ingredient_s, fodmap_dict)
        if direct_match:
            fodmap = get_fodmap(direct_match, fodmap_dict)
            print(f'\tdirect match: {direct_match} - {fodmap} FODMAP')
            if fodmap == 'high':
                return True
            direct_matches.append(ingredient)

    remaining_ingredients = []
    for ing in main_ingredients:
        if ing not in direct_matches:
            remaining_ingredients.append(ing)
    if remaining_ingredients:
        print(f'\tremaining_ingredients={remaining_ingredients!r}')

    updated_ingredients = []
    for ing in remaining_ingredients:
        updated_ingredients.append(update_single_ingredient(ing))

    for ingredient in updated_ingredients:
        nouns = get_nouns(ingredient.lower()) or [ingredient]
        for noun in nouns:
            keyword = get_singular(noun.lower())
            print(f'\tkeyword: {keyword}')
            closest_match = get_closest_match(keyword.lower(), fodmap_dict)
            fodmap = get_fodmap(closest_match, fodmap_dict)
            print(f'\tClosest match: {closest_match} - {fodmap} FODMAP')
            if fodmap == 'high':
                return True
    return False


def is_dict_in_list(target_dict, list_of_dicts):
    """
    Check if a dictionary is present in a list of dictionaries.
    """
    for d in list_of_dicts:
        if d == target_dict:
            return True
    return False


def get_fodmap(ingredient, fodmap_dict):
    """
    Get the FODMAP level of a given ingredient.
    """
    for fod in fodmap_dict:
        if fod.get('name').lower() == ingredient.lower():
            return fod['fodmap']


def update_single_ingredient(ingredient):
    """
    Update a single ingredient based on known replacements.
    """
    items_to_check = ['pork', 'chicken', 'lamb', 'fish', 'beef', 'bean', 'cashew', 'lettuce', 'mushroom']
    for item in items_to_check:
        if item in ingredient.lower():
            return item
    return ingredient.lower()


def get_direct_match(ingredient, fodmap_dict):
    """
    Find a direct match for an ingredient in the FODMAP dictionary.
    """
    for fod in fodmap_dict:
        for k, v in fod.items():
            if k == 'name' and ingredient in v.lower():
                return v


def get_closest_match(keyword, fodmap_dict):
    """
    Find the closest match for a keyword in the FODMAP dictionary.
    """
    options = []
    for fod in fodmap_dict:
        for k, v in fod.items():
            if k == 'name' and keyword in v.lower():
                options.append(v)
    if options:
        print(f'\toptions={options!r}')
        shortest_option = options[0]
        for option in options:
            if len(option) < len(shortest_option):
                shortest_option = option
        return shortest_option
    return f'{keyword} not found'


def create_dish_recipe_dict():
    """
    Create a dictionary of dish recipes from a CSV file.
    """
    csvf = 'dish_recipe.csv'
    menu = []
    with open(csvf, 'r', newline='', encoding='utf-8') as csvfile:
        dictreader = csv.DictReader(csvfile)
        for row in dictreader:
            menu.append({
                'Dish': row['Dish'],
                'Main Ingredients': row['Main Ingredients'],
                'Seasoning': row['Seasoning']
            })
    return menu


def get_fodmap_dict():
    """
    Load the FODMAP dictionary from a JSON file.
    """
    fodmapf = 'fodmap_repo.json'
    with open(fodmapf, 'r', newline='', encoding='utf-8') as fodmapfile:
        return json.load(fodmapfile)


def get_nouns(phrase):
    """
    Extract nouns from a phrase using SpaCy.
    """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(phrase)
    nouns = []
    for token in doc:
        if token.pos_ == 'NOUN':
            nouns.append(token.text)
    return nouns


def get_singular(word):
    """
    Convert a word to its singular form using Inflect.
    """
    p = inflect.engine()
    singular_word = p.singular_noun(word)
    if singular_word:
        return singular_word.lower()
    else:
        return word.lower()


def main():
    """
    Main function to generate a low FODMAP Chinese dish recipe.

    This function uses a command-line argument to determine the number of dishes to include in the menu.
    It then generates a menu by randomly selecting dishes from a predefined list, ensuring that all dishes are low in FODMAPs.
    If a selected dish contains high FODMAP ingredients, it is replaced with another dish.
    The final dish recipes are categorized as either Lunch or Dinner based on the current time of day, and it's written to a file named accordingly.

    The function performs the following steps:
    1. Parse the command-line argument to determine the number of dishes.
    2. Determine the current meal time (Lunch or Dinner) based on the current system time - Lunch: 0:00 - 14:00, Dinner for the rest of the day.
    3. Generate a random list of low FODMAP dishes up to the specified number.
    4. Write the final dish recipes to a text file, formatted with the meal time and current date.
    """
    parser = argparse.ArgumentParser(description=
        'Generate a low FODMAP menu of a specified number of dishes.')
    parser.add_argument('-n', '--number', type=int, help='Number of dishes',
        required=True)
    args = parser.parse_args()
    meal_time = determine_meal_time()
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    output_filename = f'{meal_time}_Dish_Recipe_{date_str}.txt'
    menu = create_dish_recipe_dict()
    fodmap_dict = get_fodmap_dict()
    low_fod_dishes = []
    print(
        f"""
        Please wait while the program is generating a menu of {args.number} Chinese Dishes for {meal_time}...
        """
        )
    while len(low_fod_dishes) < args.number:
        chosen_menu = random.sample(menu, k=1)
        if is_dict_in_list(chosen_menu[0], low_fod_dishes):
            continue
        dish = chosen_menu[0]
        if is_high_fodmap_dish(dish, fodmap_dict):
            print(
                f"""
                Oops! Dish name: {dish['Dish']} has high FODMAP ingredient,
                Please wait while the program is generating the next dish for you.
            """
                )
            continue
        low_fod_dishes.append(dish)
    with open(output_filename, 'w') as file:
        file.write(
            f"\n{'=' * 35} Low FODMAP Chinese Dish Recipe for {meal_time} {'=' * 35}\n\n"
            )
        for i, dish in enumerate(low_fod_dishes):
            file.write(f"{' ' * 2}{i + 1}. Dish name: {dish['Dish']}\n")
            file.write(
                f"{' ' * 5}Main Ingredients: {dish['Main Ingredients']}\n")
            file.write(f"{' ' * 5}Seasoning: {dish['Seasoning']}\n\n")
        file.write(f"{'=' * 110}\n")
    print(f'\nOutput will be saved in file: {output_filename}\n')


if __name__ == '__main__':
    main()
