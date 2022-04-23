import requests
from random import choice
from recipe import Recipe

# ------------------------------------MENU-------------------------------------------

categories = {1: "Breakfast", 2: "Dinner", 3: "Seafood", 4: "Vegetarian", 5: "Dessert"}
categories_list = [f"{k}. {v}" for k, v in categories.items()]

print("***CATEGORIES***")
[print(i) for i in categories_list]
print()

nums_of_category = int(input("Please, choose the category number of list above: "))
chosen_category = categories[nums_of_category]
# ------------------------------------MEALS-------------------------------------------

if chosen_category == "Dinner":
    chicken = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c=Chicken").json()["meals"]
    pork = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c=Pork").json()["meals"]
    beef = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c=Beef").json()["meals"]
    soup = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c=Starter").json()["meals"]
    side = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c=Side").json()["meals"]
    meals = [*chicken, *pork, *beef, *soup, *side]
else:
    meals = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={chosen_category}").json()["meals"]
# -------------------------------------DISH-------------------------------------------


def choose_dish():
    dish = choice(meals)
    return dish


def answer():
    return input("Is this dish right for you? (Yes/No): ").lower()


chosen_dish = choose_dish()
ans = 'no'

while ans != "yes":
    chosen_dish = choose_dish()
    print(chosen_dish["strMeal"].title(), end='\n\n')
    ans = answer()

dish_name = chosen_dish["strMeal"]
dish_pic = chosen_dish["strMealThumb"]
dish_id = chosen_dish["idMeal"]
# ----------------------------------INGREDIENTS-----------------------------------------

dish_details = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={dish_id}").json()["meals"]
str_ing = 'strIngredient'
ingredients = []
for i in dish_details:
    for j in i:
        if i[j] is not None and i[j] != '':
            if str_ing in j[:len(str_ing)]:
                ingredients.append(i[j].title())
            else:
                pass


def must_buy():
    print(f"For the {dish_name} you must buy next ingredients: ")
    print(' ', *ingredients, sep="\n* ", end='\n\n')
    return input("Is your fridge full of necessary ingredients? (Yes/No): ").lower()


# ----------------------------------INSTRUCTION-----------------------------------------
answer2 = must_buy()

while answer2 != "yes":
    answer2 = must_buy()
else:
    i = dish_details[0]['strInstructions']
    instruction = list(map(lambda x: x.replace('\n', '   '), i))
    instruction = ''.join(instruction)
    window = Recipe(dish_pic, instruction, dish_name)
