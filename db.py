# import pandas as pd
# import pandasql as ps
# import numpy as np
# from IPython.display import HTML
#
# input = ['lettuce','tomato']
# df = pd.read_csv("RAW_recipes.csv")
# sql_query = f"""
# SELECT *
# FROM {df}
# WHERE ingredients LIKE "lettuce"
# """.format(df)
# #
# res_df = ps.sqldf(sql_query, locals())
# HTML(res_df.to_html(escape=False))
# print(df)
# print(res_df)

import pandas as pd
import sqlite3
#
# #read the CSV
# df = pd.read_csv('RAW_recipes.csv')
# #connect to a database
# conn = sqlite3.connect("Any_Database_Name.db") #if the db does not exist, this creates a Any_Database_Name.db file in the current directory
# #store your table in the database:
# df.to_sql('df', conn)
# #read a SQL Query out of your database and into a pandas dataframe
# sql_query = """
# SELECT *
# FROM df
# WHERE ingredients LIKE "LETTUCE"
# """
# df = pd.read_sql(sql_query, conn)
# print(df)
import re
input = ['tomato','lettuce']
data = pd.read_csv('RAW_recipes.csv')

for i in range(len(input)):
    reg = '\[(.*, )*(.* )input[i](, .*)*\]'
    re.findall(reg,data['ingredients'])
print(data)
print(re)
recommend = []
# for i in range(len(input)):
#     for j in range(len(data['ingredients'])):
#         if input[i] in data['ingredients'][j]:
#             recommend.append(data['id'][j])
#
# # print(recommend)
# # print(type(data['ingredients'][0]))

\[(.*, )*.*\btomato\b(, .*)*\]
\[(.*, )*(.* )tomato(, .*)*\]