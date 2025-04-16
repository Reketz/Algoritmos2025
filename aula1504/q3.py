masmorras = [
    ["Goblin", "Orc", "Goblin"], 
    ["Lich", "Goblin", "Zumbi", "Goblin", "Goblin"],  
    ["Lich",  "Goblin", "Dragão", "Zumbi", "Goblin"]  
]
contador = 0
for sublista in masmorras:
    contador += sublista.count('Goblin')

print(f'O valor total do xp que Jin-Woo obteve é {contador * 200}')