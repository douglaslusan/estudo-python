# from turtle import Turtle, Screen
#
# my_screen = Screen()
#
# bob = Turtle()
# bob.shape('turtle')
# bob.color('blue4')
#
# my_screen.exitonclick()

from prettytable import PrettyTable

tabela = PrettyTable()
x = PrettyTable()
y = PrettyTable()
pokemon = PrettyTable()

# # Você pode adicionar dados uma linha por vez.
# x . field_names  =  [ "Nome da cidade" ,  "Área" ,  "População" ,  "Chuvas anuais" ]
# x . add_row ([ "Adelaide" ,  1295 ,  1158259 ,  600.5 ])
# x . add_row ([ "Brisbane" ,  5905 ,  1857594 ,  1146.4 ])
# x . add_row ([ "Darwin" ,  112 ,  120900 ,  1714,7 ])
# x .add_row ([ "Hobart" ,  1357 ,  205556 ,  619,5 ])
# x . add_row ([ "Sydney" ,  2058 ,  4336374 ,  1214,8 ])
# x . add_row ([ "Melbourne" ,  1566 ,  3806092 ,  646,9 ])
# x . add_row ([ "Perth" ,  5386 ,  1554769 ,  869,4 ])
# print(x)

# Quando você tem uma lista de linhas, pode adicioná-las de uma só vez com add_rows:
# y.field_names = ["Nome da cidade", "Área", "População", "Chuvas anuais"]
# y.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         [ "Sydney",  2058, 4336374, 1214.8],
#         [ "Melbourne",  1566, 3806092, 646.9],
#         [ "Perth", 5386, 1554769, 869.4],
# 	]
# )
# print(y)


# # Você também pode adicionar dados uma coluna de cada vez.
# tabela.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# tabela.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# tabela.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# tabela.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])
# print(tabela)


pokemon.field_names = ["Numero", "Pokemon", "Tipo"]
pokemon.add_rows(
    [
        ['#001', 'Chespin', 'Grass'],
        ['#002', 'Quilladin', 'Grass'],
        ['#003', 'Chesnaught', 'Grass · Fighting'],
        ['#004', 'Fennekin', 'Fire'],
        ['#005', 'Braixen', 'Fire'],
        ['#006', 'Delphox', 'Fire · Psychic'],
        ['#007', 'Froakie', 'Water'],
        ['#008', 'Frogadier', 'Water']
	]
)




print(pokemon)