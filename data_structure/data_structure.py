#using data structures: TUPLE, LIST, SET, DICTIONARY

#A TUPLE is an unchangeable list - these are always gluten free
#A LIST for the user - changeable, ordered, shopping list
#A SET of gluten-containing ingredients - fast lookup, no duplicates
#A DICTIONARY of common foods and if they are gluten-free

always_safe = ("rice", "potatoes", "fresh fruit", "fresh vegetables", "eggs")
shopping_list = ["6 apples", "milk", "bread", "12 eggs"] 
gluten_ingredients = {"wheat", "barley", "rye", "malt", "spelt", "oats (non-GF)"}
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
print("_______________________")

while True:
  item = input('Add an item (or type "done"): ').lower()
  if item == "done":
      break
  shopping_list.append(item)  
  
print("\nYour Shopping List:", shopping_list)

# _ _ _ Check each items _ _ _
print("\nChecking items for gluten risk...\n")

for item in shopping_list:
  #Check dictionary first, LOOP
  if item in food_database:
      if food_database[item]:
        print(f"{item.title()}: SAFE")
      else:
        print(f"{item.title()}: NOT SAFE")
      continue
  #Check if item is in the always_safe tuple, LOOP
  if item in always_safe:
    print(f"{item.title()}: safe (naturally gluten-free)")
      continue
  #Check if any gluten_word _ingredient appears in the item name
  if any(gluten_word in item for gluten_word in gluten_ingredients):
    print(f"{item.title()}: warning may contain gluten")
  else:
    print(f"{item.title()}: unknown (check packaging)")