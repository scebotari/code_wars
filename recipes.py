def cakes(recipe, available):
  result = float('inf')
  ingridients = recipe.keys()

  for ingridient in ingridients:
    if ingridient not in available:
      return 0

    result = min(result, available[ingridient] // recipe[ingridient])

  return result

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available), 2, 'Wrong result for example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available), 0, 'Wrong result for example #2')