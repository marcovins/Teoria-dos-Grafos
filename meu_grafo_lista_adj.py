from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *




class MeuGrafo(GrafoListaAdjacencia):

    def deletar_vertice(self, vertice):
        # Remover o vértice da lista de vértices
        novo = MeuGrafo()
        for v in self.vertices:
            if v.rotulo != vertice:
                novo.adiciona_vertice(v.rotulo)

        for a in self.arestas.values():
            if a.v1.rotulo != vertice and a.v2.rotulo != vertice:
                novo.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
        return novo

    def deletar_aresta(self,aresta):
        novo = MeuGrafo()
        for v in self.vertices:
            novo.adiciona_vertice(v.rotulo)

        for a in self.arestas.values():
            if a.rotulo != aresta:
                novo.adiciona_aresta(a.rotulo, a.v1.rotulo, a.v2.rotulo)
        return novo

    def remover_paralelas(self, copia_grafo):

        copia = copia_grafo.arestas.keys()
        for i in copia:
            aresta1 = copia_grafo.get_aresta(i)
            if copia_grafo.existe_rotulo_aresta(i):
                for j in copia:
                    aresta2 = copia_grafo.get_aresta(j)
                    if i != j and copia_grafo.existe_rotulo_aresta(j):
                        if (len(copia_grafo.vertices)) and (len(copia_grafo.arestas)):
                            if ((aresta1.v1 == aresta2.v1) and (aresta1.v2 == aresta2.v2)):
                                copia_grafo = copia_grafo.deletar_aresta(aresta1.rotulo)
                                self.remover_paralelas(copia_grafo)

                            elif ((aresta1.v1 == aresta2.v2) and (aresta1.v2 == aresta2.v1)):
                                copia_grafo = copia_grafo.deletar_aresta(aresta1.rotulo)
                                self.remover_paralelas(copia_grafo)
        return copia_grafo

    def vertices_nao_adjacentes(self):

        adjacentes = set()
        nao_adjacentes = set()
        vertices = []

        for v in self.vertices:
            vertices.append(str(v))


        for i in self.arestas.values():
            adjacentes.add(i.v1.rotulo + "-" + i.v2.rotulo)

        for v1 in vertices:
            for v2 in vertices:
                par = (v1+"-"+v2)
                par2 = (v2+"-"+v1)

                if (v1 != v2) and (par not in adjacentes) and (par2 not in adjacentes) and (par2 not in nao_adjacentes) and (par not in nao_adjacentes):
                    nao_adjacentes.add(par)

        return  nao_adjacentes

    def ha_laco(self):

        for a in self.arestas:
            if (self.arestas[a].v1) == (self.arestas[a].v2):
                return True
        return False

    def grau(self, V=''):

        cont = 0
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        for i in self.arestas.values():
            if (i.v1.rotulo == V):
                cont += 1
            if (i.v2.rotulo == V):
                cont += 1

        return cont

    def ha_paralelas(self):

        for aresta1 in self.arestas.values():
            for aresta2 in self.arestas.values():
                if (aresta1.rotulo) != (aresta2.rotulo):
                    if ((aresta1.v1 == aresta2.v1) and (aresta1.v2 == aresta2.v2)):
                        return True
                    elif ((aresta1.v1 == aresta2.v2) and (aresta1.v2 == aresta2.v1)):
                        return True
        return False

    def arestas_sobre_vertice(self, V):

        vertice = self.get_vertice(V)
        arestas = set()

        if not(self.existe_vertice(vertice)):
            raise VerticeInvalidoError

        for i in self.arestas.values():
            if (i.v1.rotulo == V) or (i.v2.rotulo == V):
                arestas.add(i.rotulo)

        return arestas

    def eh_completo(self):

        if (self.ha_laco() or self.ha_paralelas()) or (len(self.vertices) > 1 and len(self.arestas) == 0) :
            return False

        for aresta in self.arestas:
            if (self.grau(self.arestas[aresta].v1.rotulo) != (len(self.vertices)) - 1) \
                    or (self.grau(self.arestas[aresta].v2.rotulo) != (len(self.vertices)) - 1):
                return False

        return True

    def dfs(self, V=''):

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo.'.format(V))

        if self.ha_laco():
            print("Grafo com laço")
            return ValueError

        arvore = MeuGrafo()
        arvore.adiciona_vertice(V)
        vertices_visitados = set()
        vertices_visitados.add(V)

        def caminhar_grafo(V):
            for aresta in self.arestas.values():
                if aresta.v1.rotulo == V:
                    if aresta.v2.rotulo not in vertices_visitados:
                        arvore.adiciona_vertice(aresta.v2.rotulo)
                        arvore.adiciona_aresta(aresta.rotulo, V, aresta.v2.rotulo)
                        vertices_visitados.add(aresta.v2.rotulo)
                        caminhar_grafo(aresta.v2.rotulo)
                elif aresta.v2.rotulo == V:
                    if aresta.v1.rotulo not in vertices_visitados:
                        arvore.adiciona_vertice(aresta.v1.rotulo)
                        arvore.adiciona_aresta(aresta.rotulo, aresta.v1.rotulo, V)
                        vertices_visitados.add(aresta.v1.rotulo)
                        caminhar_grafo(aresta.v1.rotulo)

        caminhar_grafo(V)
        if len(arvore.vertices) != len(self.vertices):
            print("Grafo desconexo")
            return ValueError

        return arvore

    def bfs(self, V=''):

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError('O vértice {} não existe no grafo.'.format(V))

        if self.ha_laco():
            print("Grafo com laço")
            return ValueError
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
            for vertices in vertices_explorados:
                arvore.adiciona_vertice(vertices)
            for arestas_arvore in lista_arestas:
                atual = self.get_aresta(arestas_arvore)
                arvore.adiciona_aresta(atual.rotulo, atual.v1.rotulo, atual.v2.rotulo)

        pegar_arestas(V)
        construir_arvore()

        if len(arvore.vertices) != len(self.vertices):
            print("Grafo desconexo")
            return ValueError
        return arvore

    def conexo(self):

        if self.eh_completo():
            return True

        vertices = self.vertices
        arestas = list(self.arestas.keys())
        if len(arestas) == 0:
            return False

        primeira_aresta = arestas[0]
        primeira_aresta = self.get_aresta(primeira_aresta)
        inicial = primeira_aresta.v1.rotulo
        vertices_visitados = set()
        vertices_visitados.add(inicial)

        def caminhar_grafo(V):
            for aresta in self.arestas.values():
                if aresta.v1.rotulo == V:
                    if aresta.v2.rotulo not in vertices_visitados:
                        vertices_visitados.add(aresta.v2.rotulo)
                        caminhar_grafo(aresta.v2.rotulo)
                elif aresta.v2.rotulo == V:
                    if aresta.v1.rotulo not in vertices_visitados:
                        vertices_visitados.add(aresta.v1.rotulo)
                        caminhar_grafo(aresta.v1.rotulo)

        caminhar_grafo(inicial)

        if (len(vertices) != len(vertices_visitados)):
            return False

        return True

    def ha_ciclo(self):
        if self.conexo() == False:
            return False
        vertices_visitados = []
        arestas_visitadas = []
        copia_grafo = self
        vertice_ciclo = str
        caminho_ciclo = []

        def remover_grau_um(copia):
            nonlocal copia_grafo
            for i in copia:
                if (copia_grafo.existe_rotulo_vertice(i.rotulo)):
                    grau = copia_grafo.grau(i.rotulo)
                    if( (grau == 1) or (grau == 0)):
                        copia_grafo = copia_grafo.deletar_vertice(i.rotulo)
                        if (len(copia_grafo.vertices)) and (len(copia_grafo.arestas)):
                            remover_grau_um(copia_grafo.vertices)

        def caminhar_grafo(V):
            nonlocal vertice_ciclo, copia_grafo
            arestas = sorted(list(copia_grafo.arestas_sobre_vertice(V)))
            for aresta in arestas:
                if aresta not in arestas_visitadas:
                    if copia_grafo.existe_rotulo_aresta(aresta):
                        atual = copia_grafo.get_aresta(aresta)
                        v1 = atual.v1.rotulo
                        v2 = atual.v2.rotulo
                        if v1 == V:
                            if v1 not in vertices_visitados:
                                vertices_visitados.append(v1)
                                arestas_visitadas.append(aresta)
                                copia_grafo = copia_grafo.deletar_aresta(aresta)
                                caminhar_grafo(v2)
                            else:
                                vertices_visitados.append(v1)
                                vertice_ciclo = v1
                                break

                        if v2 == V:
                            if v2 not in vertices_visitados:
                                vertices_visitados.append(v2)
                                arestas_visitadas.append(aresta)
                                copia_grafo = copia_grafo.deletar_aresta(aresta)
                                caminhar_grafo(v1)
                            else:
                                vertices_visitados.append(v2)
                                vertice_ciclo = v2
                                break



        if (copia_grafo.eh_completo() == False):
            if (copia_grafo.ha_paralelas() == True):
                copia_grafo = self.remover_paralelas(copia_grafo)

        if (len(copia_grafo.vertices) and len(copia_grafo.arestas)):
            remover_grau_um(copia_grafo.vertices)
            if (len(copia_grafo.vertices) == 0  or len(copia_grafo.arestas) == 0):
                return False
        else:
            return False
        inicial = copia_grafo.vertices
        caminhar_grafo(inicial[0].rotulo)

        if len(vertices_visitados) != len(arestas_visitadas):
            posicao = vertices_visitados.index(vertice_ciclo)
            vertices_visitados = vertices_visitados[posicao:]
            for i in range(len(vertices_visitados)):
                if i == len(vertices_visitados) - 1:
                    caminho_ciclo.append(vertices_visitados[i])
                    break
                else:
                    caminho_ciclo.append(vertices_visitados[i])
                    try:
                        caminho_ciclo.append(arestas_visitadas[i])
                    except:
                        break
        else:
            for i in range(len(vertices_visitados)):
                if i == len(vertices_visitados) - 1:
                    caminho_ciclo.append(vertices_visitados[i])
                    caminho_ciclo.append(arestas_visitadas[i])
                    caminho_ciclo.append(vertices_visitados[0])
                else:
                    caminho_ciclo.append(vertices_visitados[i])
                    caminho_ciclo.append(arestas_visitadas[i])



        return caminho_ciclo

    def caminho(self, n):

        if self.ha_paralelas():
            self = self.remover_paralelas(self)

        arestas = self.arestas.keys()
        vertices = self.vertices

        if (n > len(arestas) or n == 0):
            return False

        def percorrer(V):
            arestas = sorted(list(self.arestas_sobre_vertice(V))[::-1])
            if len(arestas) == 0:
                vertices_percorridos.append(V)
                return
            if len(caminho) == (n*2 + 1):
                return

            for i in arestas:

                if i not in arestas_percorridas:
                    aresta = self.get_aresta(i)
                    v1 = aresta.v1.rotulo
                    v2 = aresta.v2.rotulo


                    if v1 == V:
                        if n == 1:
                            caminho.append(v1)
                            caminho.append(aresta.rotulo)
                            caminho.append(v2)
                            return
                        if v1 not in vertices_percorridos:
                            if v2 not in vertices_percorridos and self.grau(v2) == 1 and (len(caminho) != n*2 - 2):
                                if len(caminho) == n*2:
                                    caminho.append(v1)
                                vertices_percorridos.append(v2)
                                arestas_percorridas.append(aresta.rotulo)

                            elif v2 not in vertices_percorridos and self.grau(v2) > 1:
                                caminho.append(v1)
                                caminho.append(aresta.rotulo)
                                vertices_percorridos.append(v1)
                                arestas_percorridas.append(aresta.rotulo)
                                percorrer(v2)
                            elif v2 in vertices_percorridos and self.grau(v2) > 1:
                                caminho.pop()
                                caminho.pop()
                                caminho.pop()
                                caminho.pop()
                                vertices_percorridos.pop()
                                vertices_percorridos.pop()
                                arestas_percorridas.pop()
                                percorrer(v2)

                            elif v2 not in vertices_percorridos and self.grau(v2) == 1 and (len(caminho) == n*2 - 2):
                                caminho.append(v1)
                                caminho.append(aresta.rotulo)
                                caminho.append(v2)
                                vertices_percorridos.append(v1)
                                vertices_percorridos.append(v2)
                                arestas_percorridas.append(aresta.rotulo)
                    elif v2 == V:
                        if n == 1:
                            caminho.append(v2)
                            caminho.append(aresta.rotulo)
                            caminho.append(v1)
                            return
                        if v2 not in vertices_percorridos:
                            if v1 not in vertices_percorridos and self.grau(v1) == 1 and (len(caminho) != n*2 - 2):
                                if len(caminho) == n*2:
                                    caminho.append(v2)
                                vertices_percorridos.append(v1)
                                arestas_percorridas.append(aresta.rotulo)

                            elif v1 not in vertices_percorridos and self.grau(v1) > 1:
                                caminho.append(v2)
                                caminho.append(aresta.rotulo)
                                vertices_percorridos.append(v2)
                                arestas_percorridas.append(aresta.rotulo)
                                percorrer(v1)
                            elif v1 in vertices_percorridos and self.grau(v1) > 1:
                                caminho.pop()
                                caminho.pop()
                                caminho.pop()
                                caminho.pop()
                                vertices_percorridos.pop()
                                vertices_percorridos.pop()
                                arestas_percorridas.pop()
                                percorrer(v1)

                            elif v1 not in vertices_percorridos and self.grau(v1) == 1 and (len(caminho) == n * 2 - 2):
                                caminho.append(v1)
                                caminho.append(aresta.rotulo)
                                caminho.append(v2)
                                vertices_percorridos.append(v1)
                                vertices_percorridos.append(v2)
                                arestas_percorridas.append(aresta.rotulo)
        def ha_grau_um(vertices):
            for i in vertices:
                if self.grau(i.rotulo) == 1:
                    return (i.rotulo)

            return (vertices[0].v1.rotulo)

        vertices_percorridos = []
        arestas_percorridas = []
        caminho = []
        inicial = ha_grau_um(self.vertices)
        percorrer(inicial)

        if len(caminho) == n*2 + 1:
            return caminho
        else:
            return False


