vegan_no_nos = ['eggs', 'meat', 'milk', 'fish', 'figs']

pie_ingredients = ['flower', 'apples', 'sugar', 'eggs', 'salt']

for food in pie_ingredients:
    if food in vegan_no_nos:
        print(f'oh no cannot eat {food}! its not vegan')
    else:
        print(f'Yum I love {food}')
