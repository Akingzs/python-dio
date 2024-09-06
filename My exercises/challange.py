def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    lista_items = len(vendas)
    media_vendas = total_vendas / lista_items
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    entrada_lista = entrada.split(',')
    vendas = list(map(to_int,entrada_lista))
    return vendas
    
def to_int(n):
    return int(n)

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))