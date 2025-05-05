# Tuplas
# time_pokemon = ("Pikachu", "Charizard", "Bulbasaur", 
#                 "Squirtle", "Jigglypuff", "Snorlax")

# #time_pokemon.append("Raichu") da erro pois tupla é imutável
# #time_pokemon[0] = "Raichu" da erro pois tupla é imutável

# Sets
pokedex = {"Pikachu", "Charizard", "Bulbasaur", "Pikachu"}  
print(pokedex)

# União (time + Pokémons selvagens)
time_gui = {"Pikachu", "Charizard"}
time_allan = {"Bulbasaur", "Pidgey"}
time_total = time_gui.union(time_allan)
print(f'União dos times: {time_total}')

# Diferença (Pokémons que faltam para completar a Pokédex)
pallet_town = {"Pikachu", "Bulbasaur"}
pewter_city = {"Pikachu", "Squirtle"}
faltantes = pewter_city.difference(pallet_town)
print(f'Diferença: {faltantes}')

# Interseção (Pokémons em comum de duas regiões)
pallet_town = {"Pikachu", "Bulbasaur"}
pewter_city = {"Pikachu", "Squirtle"}
iguais = pewter_city.intersection(pallet_town)
print(f'Interseção: {iguais}')

timeA = {"Pikachu", "Bulbasaur", "Squirtle"}
timeB = {"Squirtle", "Pidgey", "Charizard"}

print(timeA | timeB)  # União
print(timeA & timeB)  # Interseção
print(timeA - timeB)  # Diferença

pokemons = ["Pikachu", "Charizard", "Bulbasaur", "Pikachu", "Charizard", "Pidgey", "Bulbasaur"]
pokedex = set(pokemons)
print(f'Pokedex => {pokedex}')

pokedexFixa = tuple(pokedex)
# pokedexFixa[0] = "Pichu" da erro pois uma tupla é imutável (inalterável)