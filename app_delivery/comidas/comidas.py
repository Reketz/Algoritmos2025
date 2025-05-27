comidas = []

def cadastrar_comida(descricao, preco, saldo):
    comida = {
        'descricao': descricao,
        'preco': preco,
        'saldo': saldo
    }

    comidas.append(comida)

def comprar_comida(descricao, quantidade):
    c_atual = None
    for c in comidas:
        if(c['descrica'] == descricao and c['saldo'] >= quantidade):
            c['saldo'] -= quantidade
            c_atual = c
            break

    if(c_atual != None):
        return float(c_atual['preco']) * quantidade
    else:
        return 0