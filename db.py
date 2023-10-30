import pandas as pd
import re
input = ['honey']
data = pd.read_csv('RAW_recipes.csv')
recommend = []
i=0
normal_reg = "\[(.*, )*.*'(, .*)*"+input[i]+"(, .*)*'(, .*)*\]"
# print(recommend)
# print(data['ingredients'][0])
# print(normal_reg)
# print(type(data['ingredients'][0]))
# if bool(re.search(normal_reg, str(data['ingredients'][0]))):
#     print('true')
# else:
#     print('false')
# test = "['winter squash', 'mexican seasoning', 'mixed spice', 'honey', 'butter', 'olive oil', 'salt']"
# if bool(re.search(normal_reg, test)):
#     print('true')
# else:
#     print('false')
d = {'name':[], 'id':[], "steps":[], "description":[],"ingredients":[]}
df = pd.DataFrame(data = d)
print(df)
for i in range(len(data['ingredients'][i])):
    if bool(re.search(normal_reg, data['ingredients'][i])):
        re.search(normal_reg, data['ingredients'][i])
        recommend.append(data['id'][i])
        print(data['ingredients'][i])
        # df.append({'name':data['name'][i]})
        # df.append({'id': data['id'][i]})
        # df.append({'steps': data['steps'][i]})
        # df.append({'description': data['description'][i]})
        # df.append({'ingredients': data['ingredients'][i]})
        #pd.concat([pd.DataFrame(data['name'][i], columns=['name'])], ignore_index=True)
print(recommend)
print(df)
# \[(.*, )*.*tomato(, .*)*egg(, .*)*\]


def createRegex():
    words = ["tomato", "orange", "banana"]
    length = len(words)
    string_words = (','.join(str(x) for x in words)).replace('[', '').replace(']', '').replace(',', '|')
    #print(string_words)
    regex = "\["
    for i in range(length):
        regex += "(.*(, .*)*({})(, .*)*)+".format(string_words)
    regex += "\]"
    print(regex)
    return regex