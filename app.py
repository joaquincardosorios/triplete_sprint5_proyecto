import streamlit as st
import pandas as pd
import plotly.express as px

# 
boardgames_data = pd.read_csv('./datasets/boardgames_ranks.csv')
boardgames_data = boardgames_data[((boardgames_data['yearpublished'] != 0))]

def categorize_game(game):
    category = 'undefined'
    categories = {
        'abstracts_rank' : 'Abstractos',
        'cgs_rank' : 'Cartas',
        'childrensgames_rank' : 'Niños',
        'familygames_rank' : 'Familia',
        'partygames_rank' : 'Fiesta',
        'strategygames_rank' : 'Estrategia',
        'thematic_rank' : 'Tematico',
        'wargames_rank' : 'De guerra'
    }
    rank_cat = 0
    for category_rank in categories.keys():
        if (not pd.isna(game[category_rank]) and category == 'undefined'):
            category = categories[category_rank]
            rank_cat = game[category_rank]
        elif not pd.isna(game[category_rank]):
            if game[category_rank] > rank_cat:
                category = categories[category_rank]
                rank_cat = game[category_rank]
    return category

boardgames_data['category'] = boardgames_data.apply(categorize_game, axis=1)
# boardgames_data_filtered = boardgames_data[boardgames_data['category']!= 'undefined']

st.header('Listado de Juegos de mesa')
col1, col2 = st.columns(2)

with col1:
    build_histogram = st.checkbox('Construir un histograma')
    build_bar_1 = st.checkbox('Construir gráfico de barra 1')
    build_bar_2 = st.checkbox('Construir gráfico de barra 2')


with col2:
    build_scatter_1 = st.checkbox('Construir gráfico de dispersión 1')
    build_scatter_2 = st.checkbox('Construir gráfico de dispersión 2')

col1, col3 , col2 = st.columns([1, 2, 1])
with col3:
    ignore_undefined = st.checkbox('Ignorar categoria Indefinida')

if ignore_undefined:
    data = boardgames_data[boardgames_data['category']!= 'undefined']
else:
    data = boardgames_data

if build_histogram:
    st.write('Histograma')
    st.write('Puntuaciones de juegos')
    
    # Crear grafico
    fig = px.histogram(
        data[data['average'] != 0], 
        x='average', nbins=20, 
        labels=dict(average="Puntucación promedio", category='Categorias')
    )
    st.plotly_chart(fig, use_container_width=True)


if build_bar_1:
    st.write('Graficós de barra')
    category_counts = data['category'].value_counts()
    fig = px.bar(
        x=category_counts.index, 
        y=category_counts.values, 
        labels={'x':'Categoría', 'y':'Cantidad de juegos'},
        title='Cantidad de juegos de mesa por categoria'
    )
    st.plotly_chart(fig, use_container_width=True)


if build_bar_2:
    st.write('Graficós de barra', align='center')
    filtered_data_age = data[(data['yearpublished'] >= 1950)]
    grouped_data = filtered_data_age.groupby(['yearpublished', 'category']).size().reset_index(name='count')
    fig = px.bar(
        grouped_data, 
        x='yearpublished', 
        y='count', 
        color='category',
        labels={'count': 'Número de Juegos', 'yearpublished': 'Año', 'category':'Categoria'},
        title='Expansión de juegos de mesa en el tiempo')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter_1:
    st.write('Graficós de barra')
    fig = px.scatter(
    data, 
    x="average", 
    y="usersrated",
    title='Relación puntuación/numero de votos',
    labels={'usersrated':'Cantidad de votos', 'average':'Puntucación promedio'}) 
    st.plotly_chart(fig, use_container_width=True)


if build_scatter_2:
    filtered_data = data[data['rank'] != 0]
    fig = px.scatter(
        filtered_data, 
        x="rank", 
        y="average", 
        color='category',
        title='Como se relaciona el ranking de un juego con su puntuacion',
        labels={'rank':'Lugar en el ranking', 'average':'Puntuación promedio'}) 
    st.plotly_chart(fig, use_container_width=True)

