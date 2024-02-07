# Estudio de lanzamientos de juegos de mesa a lo largo de los años

[Link Estudio Juegos de Mesa](https://boardsgame-analisis.onrender.com)

Para este proyecto se obtuvo la base de dato a la fecha de hoy (07/02/2024) del listado actualizado de los juegos de mesa registrados por la BGG. El dataframe tendrá las siguientes columnas:

* id -> Identificador unico de cada juego
* name -> Nombre del juego.
* yearpublished -> Año de publicación.
* rank -> Posici+on en el ranking.
* bayesaverage -> Valoración promedio bayesiana.
* average -> Valoración promedio.
* abstracts_rank -> Ranking en la categoria de abstractos
* cgs_rank -> Ranking en la categoria de juegos de cartas
* childrensgames_rank -> Ranking en la categoria de juegos para niños
* familygames_rank -> Ranking en la categoria de juegos familiares
* partygames_rank -> Ranking en la categoria de juegos de fiesta
* thematic_rank -> Ranking en la categoria de juegos tematico
* wargames_rank -> Ranking en la categoria de juegos de guerra

Se realizará un pequeño analisis exploratorio para ver algunas relaciones entre las columnas mencionada, mostrando distintos tipos de graficos.