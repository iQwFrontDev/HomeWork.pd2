import pandas as pd
import numpy as np
import re

#Задача №1

def rating(x):
    if x <= 2:
        return 'Низкий рейтинг'
    elif x <=4 and x > 2:
        return 'Средний рейтинг'

    return 'Высокий рейтинг'

df_movie = pd.read_csv('movies.csv')
df_rating = pd.read_csv('ratings.csv')
df_merged = df_movie.merge(df_rating, on = 'movieId', how='left')
rating_result = df_merged.groupby('title').mean('rating').sort_values('rating', ascending=False)
rating_result['class'] = rating_result['rating'].apply(rating)
#df_show = rating_result[['rating', 'class']]

# print(df_show.head())

#Задача №3
def production_year(year):
    keyword_list = year['title'].lower().split()
    movie_year = keyword_list[-1]
    if ')' in movie_year:
        new_s = re.sub(r"[()]", "", movie_year)
        return new_s
    else:
        return '1900'
df_merged['year'] = df_merged.apply(production_year,axis=1)
year_mean_rating = df_merged.groupby('year').mean('rating').sort_values('rating', ascending=False)
# df_show = df_merged[['title','year']]
# print(year_mean_rating.head())
#Задача №2

data_location = pd.read_csv('keywords.csv')

geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

def sorting(row):
    #разбиваем строку 'keywords' фрейма 'data_location' на список для итерации и проверки вхождения
    keyword_set = row['keyword'].lower().split()
    #В цикле итерируемся по ключам и значениям фрейма 'geo_data'
    for region, city_list in geo_data.items():
        #во вложенном цикле итерируемся по каждому элементу занчения
        for i in city_list:
            #Проверяем, есть ли элемент значения в строке 'keywords'
            if i in keyword_set:
                #Если "да", то добавляем регион
                return region
    #Если нет, то добавляем 'undefined'
    return 'undefined'
#В качестве параметра функции берем строки из фрейма 'data_location' и итерируемся по ним. Резульатат функции
# записываем в  новый столбец 'region'
data_location['region'] = data_location.apply(sorting, axis=1)
#сортируем фрейм
data_location = data_location.sort_values(['region', 'shows' ], ascending=[False, True])
# print(data_location.head())