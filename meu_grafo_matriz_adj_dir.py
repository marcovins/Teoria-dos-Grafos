from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Encontra pares de vértices que não são adjacentes, considerando grafos direcionados.
        :return: Um conjunto de strings representando pares de vértices não adjacentes.
        '''
        nao_adjacentes = set()  # Conjunto para armazenar pares de vértices não adjacentes

        # Itera por todos os pares de vértices (v1, v2)
        for v1 in self.vertices:
            for v2 in self.vertices:
                if v1 == v2:
                    continue  # Ignora pares onde v1 e v2 são o mesmo vértice

                # Verifica se existe uma aresta de v1 para v2
                existe_aresta_v1_para_v2 = False
                for aresta in self.arestas_sobre_vertice(v1.rotulo):
                    aresta_obj = self.get_aresta(aresta)
                    if aresta_obj.v2.rotulo == v2.rotulo:
                        existe_aresta_v1_para_v2 = True
                        break

                # Verifica se existe uma aresta de v2 para v1
                existe_aresta_v2_para_v1 = False
                for aresta in self.arestas_sobre_vertice(v2.rotulo):
                    aresta_obj = self.get_aresta(aresta)
                    if aresta_obj.v2.rotulo == v1.rotulo:
                        existe_aresta_v2_para_v1 = True
                        break

                # Adiciona o par de vértices ao conjunto se não forem adjacentes
                if not existe_aresta_v1_para_v2:
                    nao_adjacentes.add(f'{v1}-{v2}')

                if not existe_aresta_v2_para_v1:
                    nao_adjacentes.add(f'{v2}-{v1}')

        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        # Itera por todos os vértices do grafo
        for vertice in self.vertices:
            # Obtém todas as arestas associadas ao vértice
            arestas = self.arestas_sobre_vertice(vertice.rotulo)

            # Verifica cada aresta para ver se é um laço
            for aresta in arestas:
                aresta_obj = self.get_aresta(aresta)
                # Verifica se a aresta começa e termina no mesmo vértice
                if aresta_obj.v1.rotulo == vertice.rotulo and aresta_obj.v2.rotulo == vertice.rotulo:
                    return True  # Laço encontrado

        return False  # Nenhum laço encontrado

    class VerticeInvalidoException(Exception):
        pass

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro.
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # Verifica se o vértice existe no grafo
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas = self.arestas_sobre_vertice(V)
        cont = 0

        # Contabiliza o grau do vértice
        for i in arestas:
            aresta = self.get_aresta(i)
            # Verifica se a aresta é um laço (v1 == v2)
            if aresta.v1.rotulo == aresta.v2.rotulo:
                cont += 2  # Laços contribuem com 2 para o grau
            else:
                cont += 1  # Arestas normais contribuem com 1 para o grau

        return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo.
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        # Dicionário para contar arestas entre pares direcionados de vértices
        arestas_dict = {}

        # Itera pelos pares de vértices para verificar arestas paralelas
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if len(self.arestas[i][j]) > 1:
                    return True  # Arestas paralelas encontradas

        return False  # Nenhuma aresta paralela encontrada

    def arestas_sobre_vertice(self, V):
        '''
        Obtém todas as arestas associadas a um vértice específico.
        :param V: O rótulo do vértice para o qual as arestas devem ser obtidas
        :return: Um conjunto de rótulos de arestas associadas ao vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # Verifica se o vértice existe no grafo
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas = set()
        vertice = self.indice_do_vertice((self.get_vertice(V)))

        # Itera sobre a matriz de arestas para encontrar arestas associadas ao vértice
        for v in range(len(self.vertices)):
            for i in self.arestas[v]:
                if i.items():
                    for j in i.items():
                        if j[1].v1.rotulo == V or j[1].v2.rotulo == V:
                            arestas.add(j[0])

        return arestas

    def aresta_dir_sobre_vertice(self, V:str):
        '''
        Obtém todas as arestas associadas a um vértice específico.
        :param V: O rótulo do vértice para o qual as arestas devem ser obtidas
        :return: Um conjunto de rótulos de arestas associadas ao vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # Verifica se o vértice existe no grafo
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas = set()
        vertice = self.indice_do_vertice((self.get_vertice(V)))

        # Itera sobre a matriz de arestas para encontrar arestas associadas ao vértice
        for v in range(len(self.vertices)):
            for i in self.arestas[v]:
                if i.items():
                    for j in i.items():
                        if j[1].v1.rotulo == V:
                            arestas.add(j[0])

        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        # Um grafo é completo se não há vértices não adjacentes e não há laços
        if len(self.vertices_nao_adjacentes()) > 0 or self.ha_laco():
            return False
        return True

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo.
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        def inicializar_matriz(lista: list):
            '''
            Inicializa a matriz de alcançabilidade com zeros e adiciona arestas direcionadas.
            :param lista: A lista que será usada para criar a matriz
            '''
            qtd_vertices = len(self.vertices)
            for i in range(qtd_vertices):
                lista.append([0] * qtd_vertices)

            # Adicionando arestas direcionadas (1) à matriz
            for linha in range(len(self.arestas)):
                for coluna in range(len(self.arestas[linha])):
                    if self.arestas[linha][coluna]:
                        lista[linha][coluna] = 1

        matriz = []
        vertices = len(self.vertices)
        inicializar_matriz(matriz)

        # Algoritmo de Warshall para encontrar a matriz de alcançabilidade
        for i in range(vertices):
            for j in range(vertices):
                if matriz[j][i] == 1:
                    for k in range(vertices):
                        matriz[j][k] = max(matriz[j][k], matriz[i][k])

        return matriz

    def dijkstra(self, u:str, v:str) -> list:
        #iniciar variaveis
        vertices = {}
        arestas_percorridas = []
        caminho = []
        caminho.append(v)
        encontrado = False

        for vertice in self.vertices:
            if vertice.rotulo == u:
                vertices.update({vertice.rotulo:{'Beta': 0, 'Fi': 1, 'Pi': None}})
            else:
                vertices.update({vertice.rotulo: {'Beta': float('inf'), 'Fi': 0, 'Pi': None}})

        def percorrer(vertice:str):
            nonlocal encontrado

            vertices[vertice]['Fi'] = 1

            if vertice == v or encontrado:

                arestas = self.arestas_sobre_vertice(vertice)

                for aresta in arestas:
                    aresta = self.get_aresta(aresta)
                    if aresta.v2.rotulo == vertice:
                        if vertices[vertice]['Beta'] > (vertices[aresta.v1.rotulo]['Beta'] + aresta.peso):
                            vertices[vertice]['Beta'] = (vertices[aresta.v1.rotulo]['Beta'] + aresta.peso)
                            vertices[vertice]['Pi'] = aresta.v1.rotulo
                return
            arestas = self.aresta_dir_sobre_vertice(vertice)
            for aresta in arestas:
                if aresta in arestas_percorridas:
                    continue
                arestas_percorridas.append(aresta)
                aresta = self.get_aresta(aresta)
                if aresta.v2.rotulo != u:
                    if vertices[aresta.v2.rotulo]['Beta'] > (vertices[aresta.v1.rotulo]['Beta'] + aresta.peso):
                        vertices[aresta.v2.rotulo]['Beta'] = aresta.peso + vertices[aresta.v1.rotulo]['Beta']
                        vertices[aresta.v2.rotulo]['Pi'] = aresta.v1.rotulo
            menor = float('inf')
            proximo = None
            for aresta in arestas:
                aresta = self.get_aresta(aresta)
                if vertices[aresta.v2.rotulo]['Beta'] < menor and vertices[aresta.v2.rotulo]['Fi'] == 0:
                    menor = vertices[aresta.v2.rotulo]['Beta']
                    proximo = aresta.v2.rotulo
            if proximo is not None:
                percorrer(proximo)

        #Aplicar a lógica
        percorrer(u)
        print(vertices)

        aux = v

        while aux != None:
            if vertices[aux]['Pi'] != None:
                caminho.append(vertices[aux]['Pi'])
            aux = vertices[aux]['Pi']
        caminho.reverse()



        if len(caminho) < 2:
            return False

        return caminho

    def bellman_ford(self, u: str, v: str) -> list:
        vertices = {}
        caminho = []

        for vertice in self.vertices:
            if vertice.rotulo == u:
                vertices[vertice.rotulo] = {'Beta': 0, 'Pi': None}
            else:
                vertices[vertice.rotulo] = {'Beta': float('inf'), 'Pi': None}

        for _ in range(len(self.vertices) - 1):
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    if self.arestas[i][j].values():
                        for aresta in self.arestas[i][j].values():
                            peso = aresta.peso
                            if vertices[self.vertices[i].rotulo]['Beta'] != float('inf') and vertices[self.vertices[i].rotulo]['Beta'] + peso < vertices[self.vertices[j].rotulo]['Beta']:
                                vertices[self.vertices[j].rotulo]['Beta'] = vertices[self.vertices[i].rotulo]['Beta'] + peso
                                vertices[self.vertices[j].rotulo]['Pi'] = self.vertices[i].rotulo

        for vertice in self.vertices:
            arestas = self.arestas_sobre_vertice(vertice.rotulo)
            for aresta in arestas:
                aresta = self.get_aresta(aresta)
                u_rotulo = aresta.v1.rotulo
                v_rotulo = aresta.v2.rotulo
                peso = aresta.peso
                if vertices[u_rotulo]['Beta'] + peso < vertices[v_rotulo]['Beta']:
                    return False

        aux = v
        while aux is not None:
            caminho.append(aux)
            aux = vertices[aux]['Pi']
        caminho.reverse()

        if len(caminho) < 2:
            return False
        print(len(caminho))

        return caminho
