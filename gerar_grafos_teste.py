from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_lista_adj_dir import *
from bibgrafo.aresta import ArestaDirecionada

import os

def criar_diretorio(nome_diretorio):
    """
    Cria um diretório com o nome fornecido, caso ele não exista.

    Parâmetros:
        nome_diretorio (str): O nome do diretório a ser criado.

    Retorna:
        str: Uma mensagem indicando se o diretório foi criado ou já existia.
    """
    try:
        if not os.path.exists(nome_diretorio):
            os.makedirs(nome_diretorio)
            return f"Diretório '{nome_diretorio}' criado com sucesso."
        else:
            return f"Diretório '{nome_diretorio}' já existe."
    except Exception as e:
        return f"Ocorreu um erro ao criar o diretório: {e}"

nome_diretorio = "test_json"
resultado = criar_diretorio(nome_diretorio)
print(resultado)

'''
    Este arquivo pode ser executado para gerar os arquivos .json
    que contém os grafos a serem utilizados pelos testes unitários
    da biblioteca.
'''

vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
vertices_pb = {v: Vertice(v) for v in vertices}

'''
    Grafo da Paraíba.
'''

grafo_pb = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb, 'test_json/grafo_pb.json')

'''
    Cópia do grafo da Paraíba, para testes com o método
    __eq__ (operador '==').
'''

grafo_pb2 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb2, 'test_json/grafo_pb2.json')

'''
    Este grafo da Paraíba possui uma pequena diferença
    na primeira aresta, para testes com o método __eq__
    (operador de comparação ==).
'''
grafo_pb3 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a0', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb3, 'test_json/grafo_pb3.json')

'''
    Este grafo da Paraíba possui uma pequena diferença
    na segunda aresta para testes com o método __eq__.
'''
grafo_pb4 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['J'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb4, 'test_json/grafo_pb4.json')

'''
    Este grafo é utilizado nos testes de grafos direcionados
    para a função de detecção de arestas paralelas, contendo
    arestas bidirecionais (sendo assim, não paralelas).
'''

grafo_pb5 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['J'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a4', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['C'], vertices_pb['P']),
        ArestaDirecionada('a6', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a7', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a8', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a9', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb5, 'test_json/grafo_pb5.json')

'''
    Este grafo é um grafo da Paraíba simples, sem as arestas paralelas.
'''

grafo_pb_simples = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas([
        ArestaDirecionada('a1', vertices_pb['J'], vertices_pb['C']),
        ArestaDirecionada('a2', vertices_pb['C'], vertices_pb['E']),
        ArestaDirecionada('a3', vertices_pb['P'], vertices_pb['C']),
        ArestaDirecionada('a4', vertices_pb['T'], vertices_pb['C']),
        ArestaDirecionada('a5', vertices_pb['M'], vertices_pb['C']),
        ArestaDirecionada('a6', vertices_pb['M'], vertices_pb['T']),
        ArestaDirecionada('a7', vertices_pb['T'], vertices_pb['Z'])
    ]).build()

GrafoJSON.grafo_to_json(grafo_pb_simples, 'test_json/grafo_pb_simples.json')

'''
    Este é um grafo da Paraíba completo.
'''
grafo_pb_completo = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(vertices).arestas(True).build()

GrafoJSON.grafo_to_json(grafo_pb_completo, 'test_json/grafo_pb_completo.json')

a = Vertice('A')
b = Vertice('B')
c = Vertice('C')
d = Vertice('D')

'''
    Nesta seção, ficam os grafos que contém laços.
'''
grafo_l1 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()).vertices(2) \
    .arestas([
        ArestaDirecionada('a1', a, a),
        ArestaDirecionada('a2', b, a),
        ArestaDirecionada('a3', a, a)]).build()

GrafoJSON.grafo_to_json(grafo_l1, 'test_json/grafo_l1.json')

grafo_l2 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(4).arestas([
        ArestaDirecionada('a1', a, b),
        ArestaDirecionada('a2', b, b),
        ArestaDirecionada('a3', b, a)]).build()

GrafoJSON.grafo_to_json(grafo_l2, 'test_json/grafo_l2.json')

grafo_l3 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()) \
    .vertices(4).arestas([
        ArestaDirecionada('a1', c, a),
        ArestaDirecionada('a2', c, c),
        ArestaDirecionada('a3', d, d),
        ArestaDirecionada('a4', d, d)]).build()

GrafoJSON.grafo_to_json(grafo_l3, 'test_json/grafo_l3.json')

grafo_l4 = GrafoBuilder().tipo(GrafoListaAdjacenciaDirecionado()).vertices([Vertice('A')]).build()
