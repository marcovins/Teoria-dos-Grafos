from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def deletar_vertice(self, vertice):
        # Remover o vértice da lista de vértices
        novo = MeuGrafo()
        for v in self.vertices:
            if v.rotulo != vertice:
                novo.adiciona_vertice(v.rotulo)

        for i in self.arestas:
            for j in i:
                for a in j.values():
                    if a.v1.rotulo != vertice and a.v2.rotulo != vertice:
                        if not novo.existe_rotulo_aresta(a.rotulo):
                            novo.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
        return novo

    def deletar_aresta(self,nome):
        novo = MeuGrafo()
        for v in self.vertices:
            novo.adiciona_vertice(v.rotulo)

        for i in range(len(self.arestas)):
            for j in range(len(self.arestas)):
                aresta = self.arestas[i][j]
                if i == j:
                    continue
                for a in aresta.values():
                    if a.rotulo != nome:
                        if not novo.existe_rotulo_aresta(a.rotulo):
                            novo.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
        return novo

    def remover_paralelas(self):

        aresta = self.arestas
        copia = []
        for i in range(len(aresta)):
            for j in range(len(aresta)):
                for a in aresta[i][j].values():
                    if a.rotulo not in copia:
                        copia.append(a.rotulo)

        for i in copia:
            if self.existe_rotulo_aresta(i):
                aresta1 = self.get_aresta(i)
                for j in copia:
                    if self.existe_rotulo_aresta(j):
                        aresta2 = self.get_aresta(j)
                        if i != j:
                            if (len(self.vertices)) and (len(self.arestas)):
                                if ((aresta1.v1 == aresta2.v1) and (aresta1.v2 == aresta2.v2)):
                                    self = self.deletar_aresta(aresta1.rotulo)

                                elif ((aresta1.v1 == aresta2.v2) and (aresta1.v2 == aresta2.v1)):
                                    self = self.deletar_aresta(aresta1.rotulo)

        return self

    def remover_grau_um(self):
        copia = set()

        for i in self.vertices:
            if i.rotulo not in copia:
                copia.add(i.rotulo)

        for i in copia:
            if (self.existe_rotulo_vertice(i)):
                grau = self.grau(i)
                if ((grau == 1) or (grau == 0)):
                    self = self.deletar_vertice(i)

        return self

    def vertices_nao_adjacentes(self):

        adjacentes = set()
        nao_adjacentes = set()
        vertices = []
        arestas = []

        for v in self.vertices:
            aresta = self.arestas_sobre_vertice(v.rotulo)
            vertices.append(str(v))
            for i in aresta:
                if i not in arestas:
                    arestas.append(i)

        for v in self.vertices:
            vertices.append(str(v))

        for i in arestas:
            aresta = self.get_aresta(i)

            adjacentes.add(aresta.v1.rotulo + "-" + aresta.v2.rotulo)

        for v1 in vertices:
            for v2 in vertices:
                par = (v1 + "-" + v2)
                par2 = (v2 + "-" + v1)

                if (v1 != v2) and (par not in adjacentes) and (par2 not in adjacentes) and (
                        par2 not in nao_adjacentes) and (par not in nao_adjacentes):
                    nao_adjacentes.add(par)

        return nao_adjacentes


    def ha_laco(self):
        for i in range(len(self.arestas)):
            if len(self.arestas[i][i]) > 0:
                return True
        return False



    def grau(self, V=''):
        if not self.ha_laco():
            return len(self.arestas_sobre_vertice(V))
        else:
            quantidade = 0
            for i in range(len(self.arestas)):
                if len(self.arestas[i][i]) > 0:
                    quantidade+=len(self.arestas[i][i])
            return (len(self.arestas_sobre_vertice(V)) + quantidade)

    def ha_paralelas(self):

        for i in range(len(self.arestas)):
            for j in range(len(self.arestas)):
                if i != j:
                    if len(self.arestas[i][j]) > 1 or self.ha_laco():
                        return True
        return False

    def arestas_sobre_vertice(self, V):

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        arestas = set()
        vertice = self.indice_do_vertice((self.get_vertice(V)))
        for i in range(len(self.vertices)):
            if self.arestas[vertice][i] != None:
                for j in self.arestas[vertice][i].keys():
                    arestas.add(j)
        return arestas

    def eh_completo(self):

        if (self.ha_laco() or self.ha_paralelas()) or (len(self.vertices) > 1 and len(self.arestas) == 0):
            return False
        if len(self.vertices_nao_adjacentes()) > 0:
            return False
        return True

    def dfs(self, V=''):

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo.'.format(V))

        if self.ha_laco():
            print("Grafo com laço")
            return False

        vertices = []
        for i in self.vertices:
            vertices.append(i.rotulo)
        arvore = MeuGrafo()
        arvore.adiciona_vertice(V)
        vertices_visitados = set()
        vertices_visitados.add(V)
        arestas = []

        def caminhar_grafo(V):
            arestas = self.arestas[V]

            for i in arestas:
                for a in i.values():

                    if a.v1.rotulo == vertices[V]:
                        if a.v2.rotulo not in vertices_visitados:
                            arvore.adiciona_vertice(a.v2.rotulo)
                            arvore.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
                            vertices_visitados.add(a.v2.rotulo)
                            caminhar_grafo(vertices.index(a.v2.rotulo))
                    elif a.v2.rotulo == vertices[V]:
                        if a.v1.rotulo not in vertices_visitados:
                            arvore.adiciona_vertice(a.v1.rotulo)
                            arvore.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
                            vertices_visitados.add(a.v1.rotulo)
                            caminhar_grafo(vertices.index(a.v1.rotulo))


        caminhar_grafo(vertices.index(V))

        if len(arvore.vertices) != len(self.vertices):
            print("Grafo desconexo")
            return False

        return arvore


    def bfs(self, V=''):

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo.'.format(V))

        if self.ha_laco():
            print("Grafo com laço")
            return False
        arvore = MeuGrafo()
        vertices_visitados = set()
        vertices_explorados = set()
        lista_arestas = []
        loop = False

        def pegar_arestas(V):
            if V in vertices_visitados:
                return
            vertices_explorados.add(V)
            arestas_v = sorted(list(self.arestas_sobre_vertice(V)))
            for aresta in arestas_v:
                atual = self.get_aresta(aresta)

                if (atual.rotulo not in lista_arestas):
                    if atual.v1.rotulo == V and atual.v2.rotulo not in vertices_explorados:
                        lista_arestas.append(atual.rotulo)
                        vertices_explorados.add(atual.v2.rotulo)
                    elif atual.v2.rotulo == V and atual.v1.rotulo not in vertices_explorados:
                        lista_arestas.append(atual.rotulo)
                        vertices_explorados.add(atual.v1.rotulo)
            vertices_visitados.add(V)
            for aresta in arestas_v:
                atual = self.get_aresta(aresta)
                if V == atual.v1.rotulo:
                    if atual.v2.rotulo not in vertices_visitados:
                        pegar_arestas(atual.v2.rotulo)
                elif V == atual.v2.rotulo:
                    if atual.v1.rotulo not in vertices_visitados:
                        pegar_arestas(atual.v1.rotulo)
        def construir_arvore():
            for vertices in sorted(list(vertices_explorados)):
                arvore.adiciona_vertice(vertices)
            for arestas_arvore in lista_arestas:
                atual = self.get_aresta(arestas_arvore)
                arvore.adiciona_aresta(atual.rotulo, atual.v1.rotulo, atual.v2.rotulo)

        pegar_arestas(V)
        construir_arvore()

        if len(arvore.vertices) != len(self.vertices):
            print("Grafo desconexo")
            return False

        return arvore


    def conexo(self):
        if not self.dfs(self.vertices[0].rotulo):
            return False
        return True


    def ha_ciclo(self):

        if not self.conexo():
            return False

        sem_arestas = True

        def caminhar_grafo(rotulo):
            nonlocal arestas,caminho_ciclo

            vertices_visitados = [rotulo]
            arestas_visitadas = []
            caminho_ciclo = [rotulo]
            v = rotulo
            for i in self.vertices:
                for a in arestas:

                    if a.rotulo not in arestas_visitadas:

                        if a.v1.rotulo == v:

                            if a.v2.rotulo not in vertices_visitados and self.grau(a.v2.rotulo):
                                vertices_visitados.append(a.v2.rotulo)
                                arestas_visitadas.append(a.rotulo)
                                caminho_ciclo.append(a.rotulo)
                                caminho_ciclo.append(a.v2.rotulo)
                                v = a.v2.rotulo

                            elif a.v2.rotulo in vertices_visitados and len(vertices_visitados) > 2:
                                caminho_ciclo.append(a.rotulo)
                                posicao = caminho_ciclo.index(a.v2.rotulo)
                                caminho_ciclo.append(a.v2.rotulo)
                                caminho_ciclo = caminho_ciclo[posicao:]
                                return caminho_ciclo

                        elif a.v2.rotulo == v:
                            if a.v1.rotulo not in vertices_visitados and self.grau(a.v1.rotulo):
                                vertices_visitados.append(a.v1.rotulo)
                                arestas_visitadas.append(a.rotulo)
                                caminho_ciclo.append(a.rotulo)
                                caminho_ciclo.append(a.v1.rotulo)
                                v = a.v1.rotulo

                            elif a.v1.rotulo in vertices_visitados and len(vertices_visitados) > 2:
                                caminho_ciclo.append(a.rotulo)
                                posicao = caminho_ciclo.index(a.v1.rotulo)
                                caminho_ciclo.append(a.v1.rotulo)
                                caminho_ciclo = caminho_ciclo[posicao:]
                                return caminho_ciclo



        if self.ha_paralelas():
            self = self.remover_paralelas()
        #print(self)
        if not self.eh_completo():
            self = self.remover_grau_um()
            #print(self)
        if not len(self.vertices):
            return False
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if len(self.arestas[i][j]) > 0:
                    sem_arestas = False
        if sem_arestas:
            return False
        else:
            arestas = []
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    for a in self.arestas[i][j].values():
                        arestas.append(a)


            for i in self.vertices:
                caminho_ciclo = caminhar_grafo(i.rotulo)
                if(caminho_ciclo):
                    return caminho_ciclo

        return False

    def caminho(self, n):
        if n > len(self.vertices) - 1 or n == 0:
            return False

        if not self.conexo():
            return False

        if self.ha_paralelas():
            self = self.remover_paralelas()
        def percorrer(rotulo):
            nonlocal arestas

            vertices_visitados = [rotulo]
            arestas_visitadas = []
            caminho = [rotulo]
            v = rotulo
            for i in self.vertices:
                for a in arestas:

                    if a.rotulo not in arestas_visitadas:
                        if a.v1.rotulo == v:

                            if a.v2.rotulo not in caminho:
                                if len(caminho) == (n * 2 - 1):
                                    caminho.append(a.rotulo)
                                    caminho.append(a.v2.rotulo)
                                    return caminho

                            if (a.v2.rotulo not in vertices_visitados) and (self.grau(a.v2.rotulo) > 1):
                                vertices_visitados.append(a.v2.rotulo)
                                arestas_visitadas.append(a.rotulo)
                                caminho.append(a.rotulo)
                                caminho.append(a.v2.rotulo)
                                v = a.v2.rotulo

                        elif a.v2.rotulo == v:

                            if a.v1.rotulo not in caminho:
                                if len(caminho) == (n * 2 - 1):
                                    caminho.append(a.rotulo)
                                    caminho.append(a.v1.rotulo)
                                    return caminho

                            if (a.v1.rotulo not in vertices_visitados) and (self.grau(a.v1.rotulo) > 1):
                                vertices_visitados.append(a.v1.rotulo)
                                arestas_visitadas.append(a.rotulo)
                                caminho.append(a.rotulo)
                                caminho.append(a.v1.rotulo)
                                v = a.v1.rotulo

        arestas = []
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                for a in self.arestas[i][j].values():
                    arestas.append(a)

        for i in self.vertices:
            caminho = percorrer(i.rotulo)
            try:
                if len(caminho) == n*2 + 1:
                    return caminho
            except:
                pass

        return False

