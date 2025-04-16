monstros = ["Esqueleto", "Lobisomem", "Zumbi", "Goblin", "Demônio", "Cachorro do demonho"]
sombras = []

tamanhoDobrado = len(monstros) * 2

for i in range(1, tamanhoDobrado + 1):
    sombras.append(f"Sombra {i}")

print(sombras)