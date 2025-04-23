usuarios = []

usuarios.append(["g", 'g@email.com', '123'])
usuarios.append(["h", 'h@email.com', '323'])
usuarios.append(["j", 'j@email.com', '1311'])
usuarios.append(["l", 'l@email.com', '1233241'])
usuarios.append(["m", 'm@email.com', '12333'])
usuarios.append(["n", 'n@email.com', '123112'])

emailRemover = 'n@email.com'

indiceEncontrado = -1
for indice in range(len(usuarios)):
    if (emailRemover == usuarios[indice][1]):
        indiceEncontrado = indice

if(indiceEncontrado == -1):
    print("Não encontrado")