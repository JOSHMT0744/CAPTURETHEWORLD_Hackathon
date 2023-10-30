import pandas as pd
import re
import zipfile

def createRegex(words):
    # words = ["tomato", "orange", "banana"]
    length = len(words)
    string_words = (','.join(str(x) for x in words)).replace('[', '').replace(']', '').replace(',', '|')
    #print(string_words)
    regex = "\[(')*"
    for i in range(length):
        regex += "(.*(, '.*')*'.*({})'(, '.*')*)+".format(string_words)
    regex += "\]"
    print(regex)
    return regex

def findRecipes(input):
    input = ['lettuce','oil']
    with zipfile.ZipFile('csv_files.zip', 'r') as myzip:
        with myzip.open('archive/RAW_recipes.csv') as myfile:
            data = pd.read_csv(myfile)
    recommend = []
    i=0
    regex_string = createRegex(input)
    d = {'name':[], 'id':[], "steps":[], "description":[],"ingredients":[], "ingredient_count":[]}
    df = pd.DataFrame(data = d)
    i = 0
    count = 6 # Number of recipes to find
    while i < len(data['ingredients']) and count != 0:
        ingredient_list = data['ingredients'][i]
        if bool(re.search(regex_string, ingredient_list)):
            re.search(regex_string, ingredient_list)
            num_ingred = len(ingredient_list)
            recommend.append(data['id'][i])
            print(ingredient_list)
            new_row = {'name':data['name'][i], 'id': data['id'][i], 'steps': data['steps'][i], 'description': data['description'][i], 'ingredients': data['ingredients'][i], 'ingredient_count': num_ingred}
            df.loc[len(df)] = new_row        
            count -= 1
        i += 1
    print(recommend)
    print(df)
    top_3 = df.sort_values(by=['ingredient_count'], ascending=False).head(3)
    return top_3

