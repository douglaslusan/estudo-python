travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(pais_visitado, vezes_visitada, cidade_visitada):
	novo_pais = {}
	novo_pais['country'] = pais_visitado
	novo_pais['visits'] = vezes_visitada
	novo_pais['cities'] = cidade_visitada
	travel_log.append(novo_pais)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)