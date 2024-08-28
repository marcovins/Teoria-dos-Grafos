import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        self.g_k3 = MeuGrafo()
        self.g_k3.adiciona_vertice("A")
        self.g_k3.adiciona_vertice("B")
        self.g_k3.adiciona_vertice("C")
        self.g_k3.adiciona_aresta('a1', 'A', 'B')
        self.g_k3.adiciona_aresta('a2', 'A', 'C')
        self.g_k3.adiciona_aresta('a3', 'B', 'C')

        #Grafos de teste de busca em profundidade
        self.g_c_dfs = MeuGrafo()
        self.g_c_dfs.adiciona_vertice("C")
        self.g_c_dfs.adiciona_vertice("J")
        self.g_c_dfs.adiciona_vertice("E")
        self.g_c_dfs.adiciona_vertice("P")
        self.g_c_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_c_dfs.adiciona_aresta('a4', 'C', 'E')
        self.g_c_dfs.adiciona_aresta('a6', 'E', 'P')

        self.g_c_dfs2 = MeuGrafo()
        self.g_c_dfs2.adiciona_vertice("C")
        self.g_c_dfs2.adiciona_vertice("J")
        self.g_c_dfs2.adiciona_vertice("E")
        self.g_c_dfs2.adiciona_vertice("P")
        self.g_c_dfs2.adiciona_aresta('a1', 'C', 'J')
        self.g_c_dfs2.adiciona_aresta('a2', 'J', 'E')
        self.g_c_dfs2.adiciona_aresta('a6', 'E', 'P')

        self.g_c_dfs3 = MeuGrafo()
        self.g_c_dfs3.adiciona_vertice("C")
        self.g_c_dfs3.adiciona_vertice("J")
        self.g_c_dfs3.adiciona_vertice("E")
        self.g_c_dfs3.adiciona_vertice("P")
        self.g_c_dfs3.adiciona_aresta('a2', 'E', 'J')
        self.g_c_dfs3.adiciona_aresta('a1', 'J', 'C')
        self.g_c_dfs3.adiciona_aresta('a5', 'C', 'P')

        self.g_c_dfs4 = MeuGrafo()
        self.g_c_dfs4.adiciona_vertice("C")
        self.g_c_dfs4.adiciona_vertice("J")
        self.g_c_dfs4.adiciona_vertice("E")
        self.g_c_dfs4.adiciona_vertice("P")
        self.g_c_dfs4.adiciona_aresta('a3', 'P', 'J')
        self.g_c_dfs4.adiciona_aresta('a1', 'J', 'C')
        self.g_c_dfs4.adiciona_aresta('a4', 'C', 'E')

        self.g_p_dfs = MeuGrafo()
        self.g_p_dfs.adiciona_vertice("J")
        self.g_p_dfs.adiciona_vertice("C")
        self.g_p_dfs.adiciona_vertice("E")
        self.g_p_dfs.adiciona_vertice("P")
        self.g_p_dfs.adiciona_vertice("M")
        self.g_p_dfs.adiciona_vertice("T")
        self.g_p_dfs.adiciona_vertice("Z")
        self.g_p_dfs.adiciona_aresta('a1', 'C', 'J')
        self.g_p_dfs.adiciona_aresta('a2', 'C', 'E')
        self.g_p_dfs.adiciona_aresta('a4', 'C', 'P')
        self.g_p_dfs.adiciona_aresta('a6', 'T', 'C')
        self.g_p_dfs.adiciona_aresta('a7', 'C', 'M')
        self.g_p_dfs.adiciona_aresta('a9', 'T', 'Z')

        self.g_p_dfs2 = MeuGrafo()
        self.g_p_dfs2.adiciona_vertice("J")
        self.g_p_dfs2.adiciona_vertice("C")
        self.g_p_dfs2.adiciona_vertice("E")
        self.g_p_dfs2.adiciona_vertice("P")
        self.g_p_dfs2.adiciona_vertice("M")
        self.g_p_dfs2.adiciona_vertice("T")
        self.g_p_dfs2.adiciona_vertice("Z")
        self.g_p_dfs2.adiciona_aresta('a1', 'J', 'C')
        self.g_p_dfs2.adiciona_aresta('a2', 'C', 'E')
        self.g_p_dfs2.adiciona_aresta('a4', 'P', 'C')
        self.g_p_dfs2.adiciona_aresta('a6', 'T', 'C')
        self.g_p_dfs2.adiciona_aresta('a8', 'M', 'T')
        self.g_p_dfs2.adiciona_aresta('a9', 'T', 'Z')

        self.g_p_dfs3 = MeuGrafo()
        self.g_p_dfs3.adiciona_vertice("J")
        self.g_p_dfs3.adiciona_vertice("C")
        self.g_p_dfs3.adiciona_vertice("E")
        self.g_p_dfs3.adiciona_vertice("P")
        self.g_p_dfs3.adiciona_vertice("M")
        self.g_p_dfs3.adiciona_vertice("T")
        self.g_p_dfs3.adiciona_vertice("Z")
        self.g_p_dfs3.adiciona_aresta('a1', 'C', 'J')
        self.g_p_dfs3.adiciona_aresta('a2', 'C', 'E')
        self.g_p_dfs3.adiciona_aresta('a4', 'C', 'P')
        self.g_p_dfs3.adiciona_aresta('a6', 'T', 'C')
        self.g_p_dfs3.adiciona_aresta('a8', 'M', 'T')
        self.g_p_dfs3.adiciona_aresta('a9', 'T', 'Z')

        self.g_p_dfs4 = MeuGrafo()
        self.g_p_dfs4.adiciona_vertice("J")
        self.g_p_dfs4.adiciona_vertice("C")
        self.g_p_dfs4.adiciona_vertice("E")
        self.g_p_dfs4.adiciona_vertice("P")
        self.g_p_dfs4.adiciona_vertice("M")
        self.g_p_dfs4.adiciona_vertice("T")
        self.g_p_dfs4.adiciona_vertice("Z")
        self.g_p_dfs4.adiciona_aresta('a1', 'J', 'C')
        self.g_p_dfs4.adiciona_aresta('a2', 'C', 'E')
        self.g_p_dfs4.adiciona_aresta('a4', 'P', 'C')
        self.g_p_dfs4.adiciona_aresta('a6', 'T', 'C')
        self.g_p_dfs4.adiciona_aresta('a8', 'M', 'T')
        self.g_p_dfs4.adiciona_aresta('a9', 'T', 'Z')

        #Grafos de teste para busca em largura
        self.g_c_bfs = MeuGrafo()
        self.g_c_bfs.adiciona_vertice("J")
        self.g_c_bfs.adiciona_vertice("C")
        self.g_c_bfs.adiciona_vertice("E")
        self.g_c_bfs.adiciona_vertice("P")
        self.g_c_bfs.adiciona_aresta('a1', 'J', 'C')
        self.g_c_bfs.adiciona_aresta('a2', 'J', 'E')
        self.g_c_bfs.adiciona_aresta('a3', 'J', 'P')

        self.g_c_bfs2 = MeuGrafo()
        self.g_c_bfs2.adiciona_vertice("J")
        self.g_c_bfs2.adiciona_vertice("C")
        self.g_c_bfs2.adiciona_vertice("E")
        self.g_c_bfs2.adiciona_vertice("P")
        self.g_c_bfs2.adiciona_aresta('a1', 'J', 'C')
        self.g_c_bfs2.adiciona_aresta('a4', 'E', 'C')
        self.g_c_bfs2.adiciona_aresta('a5', 'P', 'C')

        self.g_c_bfs3 = MeuGrafo()
        self.g_c_bfs3.adiciona_vertice("J")
        self.g_c_bfs3.adiciona_vertice("C")
        self.g_c_bfs3.adiciona_vertice("E")
        self.g_c_bfs3.adiciona_vertice("P")
        self.g_c_bfs3.adiciona_aresta('a2', 'J', 'E')
        self.g_c_bfs3.adiciona_aresta('a4', 'E', 'C')
        self.g_c_bfs3.adiciona_aresta('a6', 'P', 'E')

        self.g_c_bfs4 = MeuGrafo()
        self.g_c_bfs4.adiciona_vertice("J")
        self.g_c_bfs4.adiciona_vertice("C")
        self.g_c_bfs4.adiciona_vertice("E")
        self.g_c_bfs4.adiciona_vertice("P")
        self.g_c_bfs4.adiciona_aresta('a3', 'J', 'P')
        self.g_c_bfs4.adiciona_aresta('a5', 'P', 'C')
        self.g_c_bfs4.adiciona_aresta('a6', 'P', 'E')

        self.g_p_bfs = MeuGrafo()
        self.g_p_bfs.adiciona_vertice("J")
        self.g_p_bfs.adiciona_vertice("C")
        self.g_p_bfs.adiciona_vertice("E")
        self.g_p_bfs.adiciona_vertice("P")
        self.g_p_bfs.adiciona_vertice("M")
        self.g_p_bfs.adiciona_vertice("T")
        self.g_p_bfs.adiciona_vertice("Z")
        self.g_p_bfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p_bfs.adiciona_aresta('a2', 'C', 'E')
        self.g_p_bfs.adiciona_aresta('a4', 'P', 'C')
        self.g_p_bfs.adiciona_aresta('a6', 'T', 'C')
        self.g_p_bfs.adiciona_aresta('a8', 'M', 'T')
        self.g_p_bfs.adiciona_aresta('a9', 'T', 'Z')

        self.g_p_bfs2 = MeuGrafo()
        self.g_p_bfs2.adiciona_vertice("J")
        self.g_p_bfs2.adiciona_vertice("C")
        self.g_p_bfs2.adiciona_vertice("E")
        self.g_p_bfs2.adiciona_vertice("P")
        self.g_p_bfs2.adiciona_vertice("M")
        self.g_p_bfs2.adiciona_vertice("T")
        self.g_p_bfs2.adiciona_vertice("Z")
        self.g_p_bfs2.adiciona_aresta('a1', 'J', 'C')
        self.g_p_bfs2.adiciona_aresta('a2', 'C', 'E')
        self.g_p_bfs2.adiciona_aresta('a4', 'P', 'C')
        self.g_p_bfs2.adiciona_aresta('a6', 'T', 'C')
        self.g_p_bfs2.adiciona_aresta('a7', 'M', 'C')
        self.g_p_bfs2.adiciona_aresta('a9', 'T', 'Z')

        self.g_p_bfs3 = MeuGrafo()
        self.g_p_bfs3.adiciona_vertice("J")
        self.g_p_bfs3.adiciona_vertice("C")
        self.g_p_bfs3.adiciona_vertice("E")
        self.g_p_bfs3.adiciona_vertice("P")
        self.g_p_bfs3.adiciona_vertice("M")
        self.g_p_bfs3.adiciona_vertice("T")
        self.g_p_bfs3.adiciona_vertice("Z")
        self.g_p_bfs3.adiciona_aresta('a1', 'J', 'C')
        self.g_p_bfs3.adiciona_aresta('a2', 'C', 'E')
        self.g_p_bfs3.adiciona_aresta('a4', 'P', 'C')
        self.g_p_bfs3.adiciona_aresta('a6', 'T', 'C')
        self.g_p_bfs3.adiciona_aresta('a7', 'M', 'C')
        self.g_p_bfs3.adiciona_aresta('a9', 'T', 'Z')

        self.g_p_bfs4 = MeuGrafo()
        self.g_p_bfs4.adiciona_vertice("J")
        self.g_p_bfs4.adiciona_vertice("C")
        self.g_p_bfs4.adiciona_vertice("E")
        self.g_p_bfs4.adiciona_vertice("P")
        self.g_p_bfs4.adiciona_vertice("M")
        self.g_p_bfs4.adiciona_vertice("T")
        self.g_p_bfs4.adiciona_vertice("Z")
        self.g_p_bfs4.adiciona_aresta('a1', 'J', 'C')
        self.g_p_bfs4.adiciona_aresta('a2', 'C', 'E')
        self.g_p_bfs4.adiciona_aresta('a4', 'P', 'C')
        self.g_p_bfs4.adiciona_aresta('a6', 'T', 'C')
        self.g_p_bfs4.adiciona_aresta('a7', 'M', 'C')
        self.g_p_bfs4.adiciona_aresta('a9', 'T', 'Z')

        #Grafos sem ciclos
        self.g_sem_ciclos = MeuGrafo()
        self.g_sem_ciclos.adiciona_vertice("A")
        self.g_sem_ciclos.adiciona_vertice("B")
        self.g_sem_ciclos.adiciona_vertice("C")
        self.g_sem_ciclos.adiciona_vertice("D")
        self.g_sem_ciclos.adiciona_vertice("E")
        self.g_sem_ciclos.adiciona_vertice("F")
        self.g_sem_ciclos.adiciona_vertice("G")
        self.g_sem_ciclos.adiciona_aresta('a1', 'A', 'B')
        self.g_sem_ciclos.adiciona_aresta('a2', 'A', 'C')
        self.g_sem_ciclos.adiciona_aresta('a3', 'B', 'D')
        self.g_sem_ciclos.adiciona_aresta('a4', 'B', 'E')
        self.g_sem_ciclos.adiciona_aresta('a5', 'C', 'F')
        self.g_sem_ciclos.adiciona_aresta('a6', 'C', 'G')

        self.g_sem_ciclos2 = MeuGrafo()
        self.g_sem_ciclos2.adiciona_vertice("A")
        self.g_sem_ciclos2.adiciona_vertice("B")
        self.g_sem_ciclos2.adiciona_vertice("C")
        self.g_sem_ciclos2.adiciona_vertice("D")
        self.g_sem_ciclos2.adiciona_vertice("E")
        self.g_sem_ciclos2.adiciona_vertice("F")
        self.g_sem_ciclos2.adiciona_aresta('a1', 'A', 'B')
        self.g_sem_ciclos2.adiciona_aresta('a2', 'B', 'C')
        self.g_sem_ciclos2.adiciona_aresta('a3', 'C', 'D')
        self.g_sem_ciclos2.adiciona_aresta('a4', 'D', 'E')
        self.g_sem_ciclos2.adiciona_aresta('a5', 'E', 'F')

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(),
                         {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {
                         'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {
                         'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'),
                         {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):

        #Grafo completo

        self.assertEqual(self.g_c.dfs('J'), self.g_c_dfs)
        self.assertEqual(self.g_c.dfs('C'), self.g_c_dfs2)
        self.assertEqual(self.g_c.dfs('E'), self.g_c_dfs3)
        self.assertEqual(self.g_c.dfs('P'), self.g_c_dfs4)
        self.assertEqual(self.g_c3.dfs('Único'), self.g_c3)
        self.assertEqual(self.g_c2.dfs('Nina'), self.g_c2)

        # grafo da paraiba

        self.assertEqual(self.g_p.dfs("T"), self.g_p_dfs)
        self.assertEqual(self.g_p.dfs('J'), self.g_p_dfs2)
        self.assertEqual(self.g_p.dfs('C'), self.g_p_dfs3)
        self.assertEqual(self.g_p.dfs('E'), self.g_p_dfs4)

        # Vertice invalido
        with self.assertRaises(VerticeInvalidoError):
            self.g_c.dfs('W')
            self.g_c.dfs('')

        # Grafo com laço
        self.assertEqual(self.g_l1.dfs('A'), ValueError)
        self.assertEqual(self.g_l1.dfs('B'), ValueError)
        self.assertEqual(self.g_l1.dfs('C'), ValueError)
        self.assertEqual(self.g_l1.dfs('D'), ValueError)

        # Grafo desconexo
        self.assertEqual(self.g_d.dfs('A'), ValueError)
        self.assertEqual(self.g_d.dfs('B'), ValueError)
        self.assertEqual(self.g_d.dfs('C'), ValueError)
        self.assertEqual(self.g_d.dfs('D'), ValueError)


    def test_bfs(self):

        #Grafo completo

        self.assertEqual(self.g_c.bfs('J'), self.g_c_bfs)
        self.assertEqual(self.g_c.bfs('C'), self.g_c_bfs2)
        self.assertEqual(self.g_c.bfs('E'), self.g_c_bfs3)
        self.assertEqual(self.g_c.bfs('P'), self.g_c_bfs4)
        self.assertEqual(self.g_c3.bfs('Único'), self.g_c3)
        self.assertEqual(self.g_c2.bfs('Nina'), self.g_c2)

        # Grafo da paraiba
        self.assertEqual(self.g_p.bfs('T'), self.g_p_bfs)
        self.assertEqual(self.g_p.bfs('J'), self.g_p_bfs2)
        self.assertEqual(self.g_p.bfs('C'), self.g_p_bfs3)
        self.assertEqual(self.g_p.bfs('E'), self.g_p_bfs4)

        # Vertice invalido
        with self.assertRaises(VerticeInvalidoError):
            self.g_c.bfs('W')
            self.g_c.bfs('')

        #Grafo com laço
        self.assertEqual(self.g_l1.bfs('A'), ValueError)
        self.assertEqual(self.g_l1.bfs('B'), ValueError)
        self.assertEqual(self.g_l1.bfs('C'), ValueError)
        self.assertEqual(self.g_l1.bfs('D'), ValueError)

        #Grafo desconexo
        self.assertEqual(self.g_d.bfs('A'), ValueError)
        self.assertEqual(self.g_d.bfs('B'), ValueError)
        self.assertEqual(self.g_d.bfs('C'), ValueError)
        self.assertEqual(self.g_d.bfs('D'), ValueError)

    def test_conexo(self):
        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.g_d2.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_p.conexo())

    def test_ha_ciclo(self):
        self.assertEqual(self.g_c.ha_ciclo(), ['J', 'a1', 'C', 'a4', 'E', 'a2', 'J'])
        self.assertEqual(self.g_p.ha_ciclo(),['C', 'a6', 'T', 'a8', 'M', 'a7', 'C'])
        self.assertFalse(self.g_sem_ciclos.ha_ciclo())
        self.assertFalse(self.g_sem_ciclos2.ha_ciclo())
        self.assertFalse(self.g_c2.ha_ciclo())
        self.assertFalse(self.g_c3.ha_ciclo())
        self.assertEqual(self.g_k3.ha_ciclo(), ['A', 'a1', 'B', 'a3', 'C', 'a2', 'A'])

    def test_caminho(self):
        self.assertFalse(self.g_c2.caminho(5))
        self.assertFalse(self.g_c2.caminho(4))
        self.assertFalse(self.g_c2.caminho(3))
        self.assertFalse(self.g_c2.caminho(2))
        self.assertEqual(self.g_c2.caminho(1), ['Nina', 'amiga', 'Maria'])
        self.assertFalse(self.g_c2.caminho(0))
        self.assertFalse(self.g_p.caminho(5))
        self.assertEqual(self.g_p.caminho(4), ['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertEqual(self.g_p.caminho(3), ['J', 'a1', 'C', 'a7', 'M', 'a8', 'T'])
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a3', 'E'])
        self.assertEqual(self.g_p.caminho(1), ['J', 'a1', 'C'])
        self.assertFalse(self.g_p.caminho(0))