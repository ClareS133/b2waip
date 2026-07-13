# --- Coeliac Shopping List Helper ---

# 1. A tuple of foods that are ALWAYS gluten-free (tuples = unchangeable lists)
always_safe = ("rice", "potatoes", "fresh fruit", "fresh vegetables", "eggs")

# 2. A list for the user's shopping list (lists = changeable, ordered)
shopping_list = []

# 3. A set of gluten-containing ingredients (sets = fast lookup, no duplicates)
gluten_ingredients = {"wheat", "barley", "rye", "malt", "spelt", "oats (non-GF)"}

# 4. A dictionary of common foods and whether they are gluten-free
food_database = {
    "bread": False,
    "pasta": False,
    "gluten-free bread": True,
    "gluten-free pasta": True,
    "soy sauce": False,
    "tamari": True,
    "chicken": True,
    "sausages": False,
}

print("Coeliac Shopping Helper")
print("------------------------")

while True:
    item = input("Add an item (or type 'done'): ").lower()

    if item == "done":
        break

    shopping_list.append(item)

print("\nYour Shopping List:", shopping_list)

# --- Check each item ---
print("\nChecking items for gluten risk...\n")

for item in shopping_list:

    # 1. Check dictionary first
    if item in food_database:
        if food_database[item]:
            print(f"{item.title()}: SAFE")
        else:
            print(f"{item.title()}: NOT SAFE (contains gluten)")
        continue

    # 2. Check if item is in the always-safe tuple
    if item in always_safe:
        print(f"{item.title()}: SAFE (naturally gluten-free)")
        continue

    # 3. Check if any gluten ingredient appears in the item name
    if any(gluten_word in item for gluten_word in gluten_ingredients):
        print(f"{item.title()}: WARNING may contain gluten")
    else:
        print(f"{item.title()}: UNKNOWN (check packaging)")

# --- End of Coeliac Shopping List Helper ---
# This program helps coeliac individuals check their shopping list for gluten risk.
# It uses tuples, lists, sets, and dictionaries to manage food data and provide feedback.
# Users can add items to their shopping list and receive information on whether each item is safe, not safe, or requires further checking.
# 
