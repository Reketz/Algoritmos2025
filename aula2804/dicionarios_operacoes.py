# usuarios = []

# usuarioGui = {
#     'nome': 'Gui',
#     'email': 'g@email.com',
#     'senha': '123'
# }

# usuarioAna = {
#     'nome': 'Ana',
#     'email': 'a@email.com',
#     'senha': '123321'
# }

# usuarios.append(usuarioGui)
# usuarios.append(usuarioAna)
# # email = 'g@email.com'

# # if("@" in email and email.endswith('.com')):
# #     print("Email válido")

# # for usu in usuarios:
# #     if(usu.get("email") == email):
# #         print(usu.get("nome"))

# usuario = usuarios[0]

# for chave in usuario.keys():
#     print(chave)

# for valor in usuario.values():
#     print(valor)

# for chave, valor in usuario.items():
#     print('Chave', chave, 'Valor', valor)

viagem = {
    'origem': 'Paraíba',
    'destino': 'Ceará',
    'motorista': {'nome': 'Jose', 'email': 'Jose@meia.com'},
    'vagas': 12,
    'data/hora': '26/04/2025 08:40'
}

viagemCopy = viagem.copy()
dataHora = input("Digite o nova data hora: ")
viagemCopy.update({'data/hora': dataHora})
print(viagemCopy)