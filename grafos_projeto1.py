# PROJETO 1 TEORIA DE GRAFOS
# PAÍSES DA COPA DO MUNDO
# 222029172
# Susannah Gurgel

# REFERÊNCIAS:
# https://stackoverflow.com/questions/13904636/implementing-bron-kerbosch-algorithm-in-python
# https://www.geeksforgeeks.org/find-all-cliques-of-size-k-in-an-undirected-graph/?ref=rp
# https://www.youtube.com/watch?v=132XR-RLNoY&ab_channel=AustinDsouza
# https://stackoverflow.com/questions/58044012/how-to-calculate-clustering-coefficient-of-each-node-in-the-graph-in-python-usin

# carregando, tirando os espaços vazios e ; do arquivo
entrada = open('entrada', 'r')  # caso tenha problemas, coloque o caminho completo do arquivo
entrada = [x.rstrip() for x in entrada]
entrada = [x.strip(";") for x in entrada]
entrada = [entrada.replace(" ","")for entrada in entrada]


# VARIAVEIS GLOBAIS
grafo = {}
for linha in entrada:
    key = linha.split(":")[0]
    value = linha.split(":")[1].split(",")
    grafo.update({key: value})  # GRAFO é um dicionário listando todas as ligações entre os vértices

P = grafo.keys()


# QUESTÃO 1 - algorítimo de bron-kerbosch SEM pivotamento:

def bk(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
# lista com conjuntos de nós possíveis, rejeitados e os nós que de fato compõem o clique

    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bk(P=P.intersection(grafo[v]), R=R.union([v]), X=X.intersection(grafo[v]))
        X.add(v)

listaCliques = list(bk(P))  #lista com todos os cliques maximais do grafo

# RESULTADOS QUESTÃO 1
print("\nQUESTÃO 1:\n")
print(*listaCliques, sep="\n")


# QUESTÃO 2 - cliques maximais maiores que 3, e clique máximo:
listaCliques2 = []
cliqueMaximo = []
def cliques(grafo):
    listaCliques2 = []
    for x in listaCliques:  #Separa lista com cliques com mais de 3 nós.
        if len(x) > 3:
            listaCliques2.append(x)

    for z in listaCliques2:  # Separa lista com os cliques máximos do grafo.
        if len(z) > len(max(listaCliques2)):
            cliqueMaximo.append(z)
    return listaCliques2, cliqueMaximo
a, b = cliques(grafo)
# RESULTADO QUESTÃO 2
print("\nQUESTÃO 2: ")
print("\nCliques com n > 3 : ", *a, sep="\n")
print("\nCliques maximais: ", *b, sep="\n")



# QUESTÃO 3 - coeficiente de aglomeração do grafo:
def coeficienteAglomeracao(grafo):
    n_links = 0
    coefLocal = []
    for node in grafo:
        vizinhos = [v for v in grafo[node]]  # define a lista de vizinhos em um nó
        n_vizinhos = len(vizinhos)  # define o tamanho da lista de vizinhos do nó
        if n_vizinhos > 1:  # define, dentre as ligações possíveis entre vizinhos, as ligações que são existentes no grafo
            for v in vizinhos:
                n_links += (len(set(grafo[v]) & set((grafo[node]))))
                n_links /= 2  # os links são calculados duas vezes
                coeficiente = n_links/(n_vizinhos*(n_vizinhos-1))
                coefLocal.append(coeficiente)
        else:
            coeficiente = 0
            coefLocal.append(coeficiente)  # se o nó tem apenas 1 vizinho, os vizinhos não podem ser vizinhos entre sí (apenas 1)

    return sum(coefLocal) / len(grafo)
# coeficiente é calculado pela soma dos coeficientes locais divido pelo tamanho do grafo

# RESULTADO QUESTÃO 3
print("\nQUESTÃO 3:")
print("Coeficiente de Aglomeração: ", coeficienteAglomeracao(grafo))
