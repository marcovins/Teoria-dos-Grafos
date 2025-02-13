import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

from meu_grafo_matriz_adj_dir import MeuGrafo


class TestGrafo(unittest.TestCase):

    grafo_drone_dijkstra: MeuGrafo

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

        self.g_p5 = MeuGrafo()
        self.g_p5.adiciona_vertice("J")
        self.g_p5.adiciona_vertice("C")
        self.g_p5.adiciona_vertice("E")
        self.g_p5.adiciona_vertice("P")
        self.g_p5.adiciona_vertice("M")
        self.g_p5.adiciona_vertice("T")
        self.g_p5.adiciona_vertice("Z")
        self.g_p5.adiciona_aresta('a1', 'J', 'C')
        self.g_p5.adiciona_aresta('a2', 'Z', 'J')
        self.g_p5.adiciona_aresta('a3', 'C', 'E')
        self.g_p5.adiciona_aresta('a4', 'P', 'C')
        self.g_p5.adiciona_aresta('a5', 'C', 'T')
        self.g_p5.adiciona_aresta('a6', 'T', 'C')
        self.g_p5.adiciona_aresta('a7', 'E', 'M')
        self.g_p5.adiciona_aresta('a8', 'M', 'T')
        self.g_p5.adiciona_aresta('a9', 'T', 'Z')

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
        self.g_c.adiciona_aresta('a1', 'J', 'C', 1 )
        self.g_c.adiciona_aresta('a2', 'J', 'E', 1)
        self.g_c.adiciona_aresta('a3', 'J', 'P', 10)
        self.g_c.adiciona_aresta('a4', 'E', 'C', 1)
        self.g_c.adiciona_aresta('a5', 'C', 'P', 10)
        self.g_c.adiciona_aresta('a6', 'E', 'P', 1)

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        self.g_c4 = MeuGrafo()
        self.g_c4.adiciona_vertice("J")
        self.g_c4.adiciona_vertice("C")
        self.g_c4.adiciona_vertice("E")
        self.g_c4.adiciona_vertice("P")
        self.g_c4.adiciona_aresta('a1', 'J', 'C')
        self.g_c4.adiciona_aresta('a2', 'J', 'E')
        self.g_c4.adiciona_aresta('a3', 'J', 'P')
        self.g_c4.adiciona_aresta('a4', 'C', 'J')
        self.g_c4.adiciona_aresta('a5', 'C', 'E')
        self.g_c4.adiciona_aresta('a6', 'C', 'P')
        self.g_c4.adiciona_aresta('a7', 'E', 'J')
        self.g_c4.adiciona_aresta('a8', 'E', 'C')
        self.g_c4.adiciona_aresta('a9', 'E', 'P')
        self.g_c4.adiciona_aresta('a10', 'P', 'J')
        self.g_c4.adiciona_aresta('a11', 'P', 'C')
        self.g_c4.adiciona_aresta('a12', 'P', 'E')

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

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo()
        self.g_e.adiciona_vertice("A")
        self.g_e.adiciona_vertice("B")
        self.g_e.adiciona_vertice("C")
        self.g_e.adiciona_vertice("D")
        self.g_e.adiciona_vertice("E")
        self.g_e.adiciona_aresta('1', 'A', 'B')
        self.g_e.adiciona_aresta('2', 'A', 'C')
        self.g_e.adiciona_aresta('3', 'C', 'A')
        self.g_e.adiciona_aresta('4', 'C', 'B')
        self.g_e.adiciona_aresta('10', 'C', 'B')
        self.g_e.adiciona_aresta('5', 'C', 'D')
        self.g_e.adiciona_aresta('6', 'D', 'D')
        self.g_e.adiciona_aresta('7', 'D', 'B')
        self.g_e.adiciona_aresta('8', 'D', 'E')
        self.g_e.adiciona_aresta('9', 'E', 'A')
        self.g_e.adiciona_aresta('11', 'E', 'B')

        # Grafo ABCDEFG com varios ciclos
        self.g_a = MeuGrafo()
        self.g_a.adiciona_vertice("A")
        self.g_a.adiciona_vertice("B")
        self.g_a.adiciona_vertice("C")
        self.g_a.adiciona_vertice("D")
        self.g_a.adiciona_vertice("E")
        self.g_a.adiciona_vertice("F")
        self.g_a.adiciona_vertice("G")
        self.g_a.adiciona_aresta('a1', 'A', 'B')
        self.g_a.adiciona_aresta('a2', 'B', 'C')
        self.g_a.adiciona_aresta('a3', 'C', 'D')
        self.g_a.adiciona_aresta('a4', 'D', 'E')
        self.g_a.adiciona_aresta('a5', 'E', 'F')
        self.g_a.adiciona_aresta('a6', 'F', 'G')
        self.g_a.adiciona_aresta('a7', 'G', 'A')
        self.g_a.adiciona_aresta('a8', 'B', 'D')
        self.g_a.adiciona_aresta('a9', 'C', 'F')

        # Grafo XYZWVUT com varios ciclos
        self.g_x = MeuGrafo()
        self.g_x.adiciona_vertice("X")
        self.g_x.adiciona_vertice("Y")
        self.g_x.adiciona_vertice("Z")
        self.g_x.adiciona_vertice("W")
        self.g_x.adiciona_aresta('a1', 'X', 'W')
        self.g_x.adiciona_aresta('a2', 'W', 'Y')
        self.g_x.adiciona_aresta('a3', 'Z', 'W')
        self.g_x.adiciona_aresta('a4', 'Z', 'Y')

        # Grafo LMNOPQR com varios ciclos
        self.g_r = MeuGrafo()
        self.g_r.adiciona_vertice("L")
        self.g_r.adiciona_vertice("M")
        self.g_r.adiciona_vertice("N")
        self.g_r.adiciona_vertice("O")
        self.g_r.adiciona_vertice("P")
        self.g_r.adiciona_aresta('a1', 'L', 'P')
        self.g_r.adiciona_aresta('a2', 'P', 'M')
        self.g_r.adiciona_aresta('a3', 'M', 'L')
        self.g_r.adiciona_aresta('a4', 'N', 'O')

        # Grafo ABC com ciclo completo

        self.g_c_c = MeuGrafo()
        self.g_c_c.adiciona_vertice('A')
        self.g_c_c.adiciona_vertice('B')
        self.g_c_c.adiciona_vertice('C')
        self.g_c_c.adiciona_aresta('a1', 'A', 'B')
        self.g_c_c.adiciona_aresta('a2', 'A', 'C')
        self.g_c_c.adiciona_aresta('a3', 'B', 'A')
        self.g_c_c.adiciona_aresta('a4', 'B', 'C')
        self.g_c_c.adiciona_aresta('a5', 'C', 'A')
        self.g_c_c.adiciona_aresta('a6', 'C', 'B')



        # Grafo drone
        self.grafo_drone_dijkstra = MeuGrafo()
        self.grafo_drone_dijkstra.adiciona_vertice('A')
        self.grafo_drone_dijkstra.adiciona_vertice('B')
        self.grafo_drone_dijkstra.adiciona_vertice('C')
        self.grafo_drone_dijkstra.adiciona_vertice('D')
        self.grafo_drone_dijkstra.adiciona_vertice('E')
        self.grafo_drone_dijkstra.adiciona_vertice('F')
        self.grafo_drone_dijkstra.adiciona_vertice('G')
        self.grafo_drone_dijkstra.adiciona_vertice('H')
        self.grafo_drone_dijkstra.adiciona_vertice('I')
        self.grafo_drone_dijkstra.adiciona_vertice('J')
        self.grafo_drone_dijkstra.adiciona_vertice('K')
        self.grafo_drone_dijkstra.adiciona_vertice('L')
        self.grafo_drone_dijkstra.adiciona_vertice('M')
        self.grafo_drone_dijkstra.adiciona_vertice('N')
        self.grafo_drone_dijkstra.adiciona_vertice('O')
        self.grafo_drone_dijkstra.adiciona_vertice('P')
        self.grafo_drone_dijkstra.adiciona_vertice('Q')
        self.grafo_drone_dijkstra.adiciona_vertice('R')
        self.grafo_drone_dijkstra.adiciona_vertice('S')
        self.grafo_drone_dijkstra.adiciona_vertice('T')
        self.grafo_drone_dijkstra.adiciona_vertice('U')
        self.grafo_drone_dijkstra.adiciona_vertice('V')
        self.grafo_drone_dijkstra.adiciona_vertice('W')
        self.grafo_drone_dijkstra.adiciona_vertice('X')
        self.grafo_drone_dijkstra.adiciona_vertice('Y')
        self.grafo_drone_dijkstra.adiciona_vertice('Z')
        self.grafo_drone_dijkstra.adiciona_vertice('AA')
        self.grafo_drone_dijkstra.adiciona_vertice('AB')
        self.grafo_drone_dijkstra.adiciona_vertice('AC')
        self.grafo_drone_dijkstra.adiciona_vertice('AD')
        self.grafo_drone_dijkstra.adiciona_vertice('AE')
        self.grafo_drone_dijkstra.adiciona_vertice('AF')
        self.grafo_drone_dijkstra.adiciona_vertice('AG')
        self.grafo_drone_dijkstra.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a2', 'B', 'I', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a3', 'I', 'J', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a4', 'J', 'U', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a5', 'U', 'V', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a6', 'V', 'Y', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a7', 'Y', 'X', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a8', 'X', 'Z', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a9', 'B', 'H', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a10', 'A', 'C', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a11', 'A', 'D', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a12', 'D', 'E', 4)
        self.grafo_drone_dijkstra.adiciona_aresta('a13', 'C', 'F', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a14', 'E', 'F', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a15', 'F', 'G', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a16', 'H', 'G', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a17', 'G', 'K', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a18', 'F', 'L', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a19', 'F', 'K', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a20', 'E', 'M', 4)
        self.grafo_drone_dijkstra.adiciona_aresta('a21', 'M', 'N', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a22', 'L', 'O', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a23', 'K', 'P', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a24', 'K', 'I', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a25', 'G', 'B', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a26', 'J', 'Q', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a27', 'Q', 'S', 7)
        self.grafo_drone_dijkstra.adiciona_aresta('a28', 'S', 'AC', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a29', 'AB', 'S', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a30', 'O', 'U', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a31', 'N', 'AA', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a32', 'P', 'AA', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a33', 'D', 'C', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a34', 'R', 'Q', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a35', 'P', 'R', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a36', 'P', 'U', 4)
        self.grafo_drone_dijkstra.adiciona_aresta('a37', 'U', 'R', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a38', 'R', 'T', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a39', 'T', 'W', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a40', 'W', 'U', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a41', 'V', 'AF', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a42', 'T', 'AG', 2)
        self.grafo_drone_dijkstra.adiciona_aresta('a43', 'T', 'AB', 1)
        self.grafo_drone_dijkstra.adiciona_aresta('a44', 'Y', 'W', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a45', 'AC', 'AD', 4)
        self.grafo_drone_dijkstra.adiciona_aresta('a46', 'AD', 'X', 3)
        self.grafo_drone_dijkstra.adiciona_aresta('a47', 'X', 'AE', 2)

        #Grafos para testar dijkstra
        self.grafo_dijkstra = MeuGrafo()
        self.grafo_dijkstra.adiciona_vertice('A')
        self.grafo_dijkstra.adiciona_vertice('B')
        self.grafo_dijkstra.adiciona_vertice('C')
        self.grafo_dijkstra.adiciona_vertice('D')
        self.grafo_dijkstra.adiciona_vertice('E')
        self.grafo_dijkstra.adiciona_aresta('a1', 'A', 'B', 2)
        self.grafo_dijkstra.adiciona_aresta('a2', 'B', 'C', 5)
        self.grafo_dijkstra.adiciona_aresta('a3', 'B', 'D', 7)
        self.grafo_dijkstra.adiciona_aresta('a4', 'C', 'E', 4)
        self.grafo_dijkstra.adiciona_aresta('a5', 'D', 'E', 1)
        self.grafo_dijkstra.adiciona_aresta('a6', 'A', 'E', 20)

        self.grafo_dijkstra2 = MeuGrafo()

        # Adicionando vértices
        for vertice in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF"]:
            self.grafo_dijkstra2.adiciona_vertice(vertice)

        # Adicionando arestas com pesos
        # Arestas do caminho de menor peso
        self.grafo_dijkstra2.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_dijkstra2.adiciona_aresta('a2', 'B', 'J', 1)
        self.grafo_dijkstra2.adiciona_aresta('a3', 'J', 'P', 1)
        self.grafo_dijkstra2.adiciona_aresta('a4', 'P', 'U', 1)
        self.grafo_dijkstra2.adiciona_aresta('a5', 'U', 'Y', 1)
        self.grafo_dijkstra2.adiciona_aresta('a6', 'Y', 'Z', 1)

        # Outras arestas com pesos maiores
        self.grafo_dijkstra2.adiciona_aresta('a7', 'A', 'C', 2)
        self.grafo_dijkstra2.adiciona_aresta('a8', 'A', 'D', 3)
        self.grafo_dijkstra2.adiciona_aresta('a9', 'D', 'E', 4)
        self.grafo_dijkstra2.adiciona_aresta('a10', 'C', 'F', 5)
        self.grafo_dijkstra2.adiciona_aresta('a11', 'F', 'G', 6)
        self.grafo_dijkstra2.adiciona_aresta('a12', 'G', 'B', 7)
        self.grafo_dijkstra2.adiciona_aresta('a13', 'G', 'H', 8)
        self.grafo_dijkstra2.adiciona_aresta('a14', 'B', 'H', 9)
        self.grafo_dijkstra2.adiciona_aresta('a15', 'G', 'I', 10)
        self.grafo_dijkstra2.adiciona_aresta('a16', 'I', 'J', 11)
        self.grafo_dijkstra2.adiciona_aresta('a17', 'F', 'K', 12)
        self.grafo_dijkstra2.adiciona_aresta('a18', 'K', 'L', 13)
        self.grafo_dijkstra2.adiciona_aresta('a19', 'L', 'M', 14)
        self.grafo_dijkstra2.adiciona_aresta('a20', 'M', 'N', 15)
        self.grafo_dijkstra2.adiciona_aresta('a21', 'K', 'O', 16)
        self.grafo_dijkstra2.adiciona_aresta('a22', 'O', 'P', 17)
        self.grafo_dijkstra2.adiciona_aresta('a23', 'P', 'Q', 18)
        self.grafo_dijkstra2.adiciona_aresta('a24', 'Q', 'R', 19)
        self.grafo_dijkstra2.adiciona_aresta('a25', 'R', 'S', 20)
        self.grafo_dijkstra2.adiciona_aresta('a26', 'S', 'T', 21)
        self.grafo_dijkstra2.adiciona_aresta('a27', 'T', 'U', 22)
        self.grafo_dijkstra2.adiciona_aresta('a28', 'U', 'V', 23)
        self.grafo_dijkstra2.adiciona_aresta('a29', 'V', 'W', 24)
        self.grafo_dijkstra2.adiciona_aresta('a30', 'W', 'X', 25)
        self.grafo_dijkstra2.adiciona_aresta('a31', 'X', 'Y', 26)
        self.grafo_dijkstra2.adiciona_aresta('a32', 'Y', 'AF', 27)
        self.grafo_dijkstra2.adiciona_aresta('a33', 'X', 'AC', 28)
        self.grafo_dijkstra2.adiciona_aresta('a34', 'AC', 'AB', 29)
        self.grafo_dijkstra2.adiciona_aresta('a35', 'AB', 'S', 30)
        self.grafo_dijkstra2.adiciona_aresta('a36', 'W', 'AD', 31)
        self.grafo_dijkstra2.adiciona_aresta('a37', 'AD', 'AE', 32)
        self.grafo_dijkstra2.adiciona_aresta('a38', 'AE', 'Z', 33)
        self.grafo_dijkstra2.adiciona_aresta('a39', 'Q', 'H', 34)
        self.grafo_dijkstra2.adiciona_aresta('a40', 'L', 'N', 35)
        self.grafo_dijkstra2.adiciona_aresta('a41', 'M', 'AA', 36)
        self.grafo_dijkstra2.adiciona_aresta('a42', 'AA', 'AF', 37)

        # Grafo simples para testar djikstra
        self.grafo_simples = MeuGrafo()
        self.grafo_simples.adiciona_vertice('A')
        self.grafo_simples.adiciona_vertice('B')
        self.grafo_simples.adiciona_vertice('C')
        self.grafo_simples.adiciona_vertice('D')

        self.grafo_simples.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_simples.adiciona_aresta('a2', 'B', 'C', 2)
        self.grafo_simples.adiciona_aresta('a3', 'A', 'D', 4)
        self.grafo_simples.adiciona_aresta('a4', 'D', 'C', 1)

        # Grafo com caminhos alternativos

        self.grafo_caminhos_alternativos = MeuGrafo()
        self.grafo_caminhos_alternativos.adiciona_vertice('A')
        self.grafo_caminhos_alternativos.adiciona_vertice('B')
        self.grafo_caminhos_alternativos.adiciona_vertice('C')
        self.grafo_caminhos_alternativos.adiciona_vertice('D')
        self.grafo_caminhos_alternativos.adiciona_vertice('E')

        self.grafo_caminhos_alternativos.adiciona_aresta('a1', 'A', 'B', 2)
        self.grafo_caminhos_alternativos.adiciona_aresta('a2', 'A', 'C', 4)
        self.grafo_caminhos_alternativos.adiciona_aresta('a3', 'B', 'C', 1)
        self.grafo_caminhos_alternativos.adiciona_aresta('a4', 'B', 'D', 7)
        self.grafo_caminhos_alternativos.adiciona_aresta('a5', 'C', 'D', 3)
        self.grafo_caminhos_alternativos.adiciona_aresta('a6', 'D', 'E', 1)
        self.grafo_caminhos_alternativos.adiciona_aresta('a7', 'C', 'E', 5)

        # Grafo com ciclos

        self.grafo_com_ciclos = MeuGrafo()
        self.grafo_com_ciclos.adiciona_vertice('A')
        self.grafo_com_ciclos.adiciona_vertice('B')
        self.grafo_com_ciclos.adiciona_vertice('C')
        self.grafo_com_ciclos.adiciona_vertice('D')

        self.grafo_com_ciclos.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_com_ciclos.adiciona_aresta('a2', 'B', 'C', 2)
        self.grafo_com_ciclos.adiciona_aresta('a3', 'C', 'D', 1)
        self.grafo_com_ciclos.adiciona_aresta('a4', 'D', 'B', 2)  # Ciclo: B -> C -> D -> B
        self.grafo_com_ciclos.adiciona_aresta('a5', 'A', 'D', 4)

        # Grafo com complexo
        self.grafo_complexo = MeuGrafo()
        self.grafo_complexo.adiciona_vertice('A')
        self.grafo_complexo.adiciona_vertice('B')
        self.grafo_complexo.adiciona_vertice('C')
        self.grafo_complexo.adiciona_vertice('D')
        self.grafo_complexo.adiciona_vertice('E')
        self.grafo_complexo.adiciona_vertice('F')

        self.grafo_complexo.adiciona_aresta('a1', 'A', 'B', 3)
        self.grafo_complexo.adiciona_aresta('a2', 'A', 'C', 1)
        self.grafo_complexo.adiciona_aresta('a3', 'B', 'C', 7)
        self.grafo_complexo.adiciona_aresta('a4', 'B', 'D', 5)
        self.grafo_complexo.adiciona_aresta('a5', 'C', 'E', 2)
        self.grafo_complexo.adiciona_aresta('a6', 'D', 'E', 2)
        self.grafo_complexo.adiciona_aresta('a7', 'D', 'F', 1)
        self.grafo_complexo.adiciona_aresta('a8', 'E', 'F', 3)


        #Grafo com arestas de peso zero
        self.grafo_peso_zero = MeuGrafo()
        self.grafo_peso_zero.adiciona_vertice('A')
        self.grafo_peso_zero.adiciona_vertice('B')
        self.grafo_peso_zero.adiciona_vertice('C')
        self.grafo_peso_zero.adiciona_vertice('D')

        self.grafo_peso_zero.adiciona_aresta('a1', 'A', 'B', 0)
        self.grafo_peso_zero.adiciona_aresta('a2', 'B', 'C', 0)
        self.grafo_peso_zero.adiciona_aresta('a3', 'C', 'D', 1)
        self.grafo_peso_zero.adiciona_aresta('a4', 'A', 'D', 2)

        # Grafo para teste bellman ford
        # Grafo drone
        self.grafo_drone_bellman = MeuGrafo()
        self.grafo_drone_bellman.adiciona_vertice('A')
        self.grafo_drone_bellman.adiciona_vertice('B')
        self.grafo_drone_bellman.adiciona_vertice('C')
        self.grafo_drone_bellman.adiciona_vertice('D')
        self.grafo_drone_bellman.adiciona_vertice('E')
        self.grafo_drone_bellman.adiciona_vertice('F')
        self.grafo_drone_bellman.adiciona_vertice('G')
        self.grafo_drone_bellman.adiciona_vertice('H')
        self.grafo_drone_bellman.adiciona_vertice('I')
        self.grafo_drone_bellman.adiciona_vertice('J')
        self.grafo_drone_bellman.adiciona_vertice('K')
        self.grafo_drone_bellman.adiciona_vertice('L')
        self.grafo_drone_bellman.adiciona_vertice('M')
        self.grafo_drone_bellman.adiciona_vertice('N')
        self.grafo_drone_bellman.adiciona_vertice('O')
        self.grafo_drone_bellman.adiciona_vertice('P')
        self.grafo_drone_bellman.adiciona_vertice('Q')
        self.grafo_drone_bellman.adiciona_vertice('R')
        self.grafo_drone_bellman.adiciona_vertice('S')
        self.grafo_drone_bellman.adiciona_vertice('T')
        self.grafo_drone_bellman.adiciona_vertice('U')
        self.grafo_drone_bellman.adiciona_vertice('V')
        self.grafo_drone_bellman.adiciona_vertice('W')
        self.grafo_drone_bellman.adiciona_vertice('X')
        self.grafo_drone_bellman.adiciona_vertice('Y')
        self.grafo_drone_bellman.adiciona_vertice('Z')
        self.grafo_drone_bellman.adiciona_vertice('AA')
        self.grafo_drone_bellman.adiciona_vertice('AB')
        self.grafo_drone_bellman.adiciona_vertice('AC')
        self.grafo_drone_bellman.adiciona_vertice('AD')
        self.grafo_drone_bellman.adiciona_vertice('AE')
        self.grafo_drone_bellman.adiciona_vertice('AF')
        self.grafo_drone_bellman.adiciona_vertice('AG')
        self.grafo_drone_bellman.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_drone_bellman.adiciona_aresta('a2', 'B', 'I', 1)
        self.grafo_drone_bellman.adiciona_aresta('a3', 'I', 'J', 1)
        self.grafo_drone_bellman.adiciona_aresta('a4', 'J', 'U', 1)
        self.grafo_drone_bellman.adiciona_aresta('a5', 'U', 'V', 1)
        self.grafo_drone_bellman.adiciona_aresta('a6', 'V', 'Y', 1)
        self.grafo_drone_bellman.adiciona_aresta('a7', 'Y', 'X', 1)
        self.grafo_drone_bellman.adiciona_aresta('a8', 'X', 'Z', 1)
        self.grafo_drone_bellman.adiciona_aresta('a9', 'B', 'H', -1)
        self.grafo_drone_bellman.adiciona_aresta('a10', 'A', 'C', 3)
        self.grafo_drone_bellman.adiciona_aresta('a11', 'A', 'D', 2)
        self.grafo_drone_bellman.adiciona_aresta('a12', 'D', 'E', 4)
        self.grafo_drone_bellman.adiciona_aresta('a13', 'C', 'F', -2)
        self.grafo_drone_bellman.adiciona_aresta('a14', 'E', 'F', 2)
        self.grafo_drone_bellman.adiciona_aresta('a15', 'F', 'G', 3)
        self.grafo_drone_bellman.adiciona_aresta('a16', 'H', 'G', 2)
        self.grafo_drone_bellman.adiciona_aresta('a17', 'G', 'K', 2)
        self.grafo_drone_bellman.adiciona_aresta('a18', 'F', 'L', 2)
        self.grafo_drone_bellman.adiciona_aresta('a19', 'F', 'K', 3)
        self.grafo_drone_bellman.adiciona_aresta('a20', 'E', 'M', 4)
        self.grafo_drone_bellman.adiciona_aresta('a21', 'M', 'N', 3)
        self.grafo_drone_bellman.adiciona_aresta('a22', 'L', 'O', 3)
        self.grafo_drone_bellman.adiciona_aresta('a23', 'K', 'P', 2)
        self.grafo_drone_bellman.adiciona_aresta('a24', 'K', 'I', 3)
        self.grafo_drone_bellman.adiciona_aresta('a25', 'G', 'B', 2)
        self.grafo_drone_bellman.adiciona_aresta('a26', 'J', 'Q', 3)
        self.grafo_drone_bellman.adiciona_aresta('a27', 'Q', 'S', 7)
        self.grafo_drone_bellman.adiciona_aresta('a28', 'S', 'AC', 2)
        self.grafo_drone_bellman.adiciona_aresta('a29', 'AB', 'S', 3)
        self.grafo_drone_bellman.adiciona_aresta('a30', 'O', 'U', 3)
        self.grafo_drone_bellman.adiciona_aresta('a31', 'N', 'AA', 3)
        self.grafo_drone_bellman.adiciona_aresta('a32', 'P', 'AA', 2)
        self.grafo_drone_bellman.adiciona_aresta('a33', 'D', 'C', 2)
        self.grafo_drone_bellman.adiciona_aresta('a34', 'R', 'Q', 3)
        self.grafo_drone_bellman.adiciona_aresta('a35', 'P', 'R', 2)
        self.grafo_drone_bellman.adiciona_aresta('a36', 'P', 'U', 4)
        self.grafo_drone_bellman.adiciona_aresta('a37', 'U', 'R', 3)
        self.grafo_drone_bellman.adiciona_aresta('a38', 'R', 'T', -1)
        self.grafo_drone_bellman.adiciona_aresta('a39', 'T', 'W', 1)
        self.grafo_drone_bellman.adiciona_aresta('a40', 'W', 'U', 2)
        self.grafo_drone_bellman.adiciona_aresta('a41', 'V', 'AF', 2)
        self.grafo_drone_bellman.adiciona_aresta('a42', 'T', 'AG', 2)
        self.grafo_drone_bellman.adiciona_aresta('a43', 'T', 'AB', 1)
        self.grafo_drone_bellman.adiciona_aresta('a44', 'Y', 'W', 3)
        self.grafo_drone_bellman.adiciona_aresta('a45', 'AC', 'AD', 4)
        self.grafo_drone_bellman.adiciona_aresta('a46', 'AD', 'X', 3)
        self.grafo_drone_bellman.adiciona_aresta('a47', 'X', 'AE', 2)

        # Grafo com ciclo negativo

        self.grafo_ciclo_negativo = MeuGrafo()
        self.grafo_ciclo_negativo.adiciona_vertice('A')
        self.grafo_ciclo_negativo.adiciona_vertice('B')
        self.grafo_ciclo_negativo.adiciona_vertice('C')
        self.grafo_ciclo_negativo.adiciona_vertice('D')
        self.grafo_ciclo_negativo.adiciona_vertice('E')
        self.grafo_ciclo_negativo.adiciona_vertice('F')
        self.grafo_ciclo_negativo.adiciona_vertice('G')

        self.grafo_ciclo_negativo.adiciona_aresta('a1', 'A', 'B', 2)
        self.grafo_ciclo_negativo.adiciona_aresta('a2', 'B', 'C', 3)
        self.grafo_ciclo_negativo.adiciona_aresta('a3', 'C', 'D', -6)  # Ciclo negativo começa aqui
        self.grafo_ciclo_negativo.adiciona_aresta('a4', 'D', 'E', 1)
        self.grafo_ciclo_negativo.adiciona_aresta('a5', 'E', 'F', 2)
        self.grafo_ciclo_negativo.adiciona_aresta('a6', 'F', 'G', 2)
        self.grafo_ciclo_negativo.adiciona_aresta('a7', 'G', 'C', 1)  # Fechamento do ciclo negativo

        self.grafo_ciclo_negativo.adiciona_aresta('a8', 'A', 'D', 5)
        self.grafo_ciclo_negativo.adiciona_aresta('a9', 'B', 'E', 1)
        self.grafo_ciclo_negativo.adiciona_aresta('a10', 'C', 'F', 4)
        self.grafo_ciclo_negativo.adiciona_aresta('a11', 'D', 'G', 2)
        self.grafo_ciclo_negativo.adiciona_aresta('a12', 'E', 'A', 3)
        self.grafo_ciclo_negativo.adiciona_aresta('a13', 'F', 'B', -2)  # Outra aresta negativa
        self.grafo_ciclo_negativo.adiciona_aresta('a14', 'G', 'A', 4)

        # Grafo sem ciclo para bellman ford

        self.grafo_sem_ciclo_negativo = MeuGrafo()
        self.grafo_sem_ciclo_negativo.adiciona_vertice('A')
        self.grafo_sem_ciclo_negativo.adiciona_vertice('B')
        self.grafo_sem_ciclo_negativo.adiciona_vertice('C')
        self.grafo_sem_ciclo_negativo.adiciona_vertice('D')

        self.grafo_sem_ciclo_negativo.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_sem_ciclo_negativo.adiciona_aresta('a2', 'B', 'C', 2)
        self.grafo_sem_ciclo_negativo.adiciona_aresta('a3', 'C', 'D', 1)
        self.grafo_sem_ciclo_negativo.adiciona_aresta('a4', 'A', 'D', 4)

        # Grafo com ciclo negativo para testar o bellman ford

        self.grafo_ciclo_negativo = MeuGrafo()
        self.grafo_ciclo_negativo.adiciona_vertice('A')
        self.grafo_ciclo_negativo.adiciona_vertice('B')
        self.grafo_ciclo_negativo.adiciona_vertice('C')
        self.grafo_ciclo_negativo.adiciona_vertice('D')

        self.grafo_ciclo_negativo.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_ciclo_negativo.adiciona_aresta('a2', 'B', 'C', -2)
        self.grafo_ciclo_negativo.adiciona_aresta('a3', 'C', 'D', 1)
        self.grafo_ciclo_negativo.adiciona_aresta('a4', 'D', 'B', -1)  # Ciclo negativo: B -> C -> D -> B

        # Ciclo negativo e varios caminhos

        self.grafo_ciclo_negativo_multiplo = MeuGrafo()
        self.grafo_ciclo_negativo_multiplo.adiciona_vertice('A')
        self.grafo_ciclo_negativo_multiplo.adiciona_vertice('B')
        self.grafo_ciclo_negativo_multiplo.adiciona_vertice('C')
        self.grafo_ciclo_negativo_multiplo.adiciona_vertice('D')
        self.grafo_ciclo_negativo_multiplo.adiciona_vertice('E')

        self.grafo_ciclo_negativo_multiplo.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_ciclo_negativo_multiplo.adiciona_aresta('a2', 'B', 'C', -2)
        self.grafo_ciclo_negativo_multiplo.adiciona_aresta('a3', 'C', 'D', 1)
        self.grafo_ciclo_negativo_multiplo.adiciona_aresta('a4', 'D', 'B', -1)  # Ciclo negativo: B -> C -> D -> B
        self.grafo_ciclo_negativo_multiplo.adiciona_aresta('a5', 'A', 'D', 4)
        self.grafo_ciclo_negativo_multiplo.adiciona_aresta('a6', 'D', 'E', 2)
        self.grafo_ciclo_negativo_multiplo.adiciona_aresta('a7', 'E', 'C', 1)  # Outro caminho para C


        # Múltiplos caminhos e ciclo negativo
        self.grafo_multiplos_ciclos_negativos = MeuGrafo()
        self.grafo_multiplos_ciclos_negativos.adiciona_vertice('A')
        self.grafo_multiplos_ciclos_negativos.adiciona_vertice('B')
        self.grafo_multiplos_ciclos_negativos.adiciona_vertice('C')
        self.grafo_multiplos_ciclos_negativos.adiciona_vertice('D')
        self.grafo_multiplos_ciclos_negativos.adiciona_vertice('E')

        self.grafo_multiplos_ciclos_negativos.adiciona_aresta('a1', 'A', 'B', 1)
        self.grafo_multiplos_ciclos_negativos.adiciona_aresta('a2', 'B', 'C', -2)
        self.grafo_multiplos_ciclos_negativos.adiciona_aresta('a3', 'C', 'A', -1)  # Ciclo negativo: A -> B -> C -> A
        self.grafo_multiplos_ciclos_negativos.adiciona_aresta('a4', 'B', 'D', 4)
        self.grafo_multiplos_ciclos_negativos.adiciona_aresta('a5', 'D', 'E', 2)
        self.grafo_multiplos_ciclos_negativos.adiciona_aresta('a6', 'E', 'C',-3)  # Outro ciclo negativo: C -> E -> D -> B -> C

        # Apenas ciclos negativos

        self.grafo_apenas_ciclos_negativos = MeuGrafo()
        self.grafo_apenas_ciclos_negativos.adiciona_vertice('A')
        self.grafo_apenas_ciclos_negativos.adiciona_vertice('B')
        self.grafo_apenas_ciclos_negativos.adiciona_vertice('C')

        self.grafo_apenas_ciclos_negativos.adiciona_aresta('a1', 'A', 'B', -1)
        self.grafo_apenas_ciclos_negativos.adiciona_aresta('a2', 'B', 'C', -1)
        self.grafo_apenas_ciclos_negativos.adiciona_aresta('a3', 'C', 'A', -1)  # Ciclo negativo: A -> B -> C -> A

        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        # Matriz grafo paraiba sem Paralelas
        self.g_p_m2 = self.constroi_matriz(self.g_p_sem_paralelas)
        self.g_p_m2[0][1] = 1
        self.g_p_m2[0][2] = 1
        self.g_p_m2[1][2] = 1
        self.g_p_m2[3][1] = 1
        self.g_p_m2[3][2] = 1
        self.g_p_m2[4][1] = 1
        self.g_p_m2[4][2] = 1
        self.g_p_m2[4][5] = 1
        self.g_p_m2[4][6] = 1
        self.g_p_m2[5][1] = 1
        self.g_p_m2[5][2] = 1
        self.g_p_m2[5][6] = 1

        # Matriz grafo paraiba com ciclo
        self.g_p_m3 = self.constroi_matriz(self.g_p5)
        self.g_p_m3[0][0] = 1
        self.g_p_m3[0][1] = 1
        self.g_p_m3[0][2] = 1
        self.g_p_m3[0][4] = 1
        self.g_p_m3[0][5] = 1
        self.g_p_m3[0][6] = 1
        self.g_p_m3[1][0] = 1
        self.g_p_m3[1][1] = 1
        self.g_p_m3[1][2] = 1
        self.g_p_m3[1][4] = 1
        self.g_p_m3[1][5] = 1
        self.g_p_m3[1][6] = 1
        self.g_p_m3[2][0] = 1
        self.g_p_m3[2][1] = 1
        self.g_p_m3[2][2] = 1
        self.g_p_m3[2][4] = 1
        self.g_p_m3[2][5] = 1
        self.g_p_m3[2][6] = 1
        self.g_p_m3[3][0] = 1
        self.g_p_m3[3][1] = 1
        self.g_p_m3[3][2] = 1
        self.g_p_m3[3][4] = 1
        self.g_p_m3[3][5] = 1
        self.g_p_m3[3][6] = 1
        self.g_p_m3[4][0] = 1
        self.g_p_m3[4][1] = 1
        self.g_p_m3[4][2] = 1
        self.g_p_m3[4][4] = 1
        self.g_p_m3[4][5] = 1
        self.g_p_m3[4][6] = 1
        self.g_p_m3[5][0] = 1
        self.g_p_m3[5][1] = 1
        self.g_p_m3[5][2] = 1
        self.g_p_m3[5][4] = 1
        self.g_p_m3[5][5] = 1
        self.g_p_m3[5][6] = 1
        self.g_p_m3[6][0] = 1
        self.g_p_m3[6][1] = 1
        self.g_p_m3[6][2] = 1
        self.g_p_m3[6][4] = 1
        self.g_p_m3[6][5] = 1
        self.g_p_m3[6][6] = 1

        # Matriz grafo completo
        self.g_c_m = self.constroi_matriz(self.g_c)
        self.g_c_m[0][1] = 1
        self.g_c_m[0][2] = 1
        self.g_c_m[0][3] = 1
        self.g_c_m[2][1] = 1
        self.g_c_m[3][1] = 1
        self.g_c_m[3][2] = 1

        # Matriz grafo com laço
        self.g_l3_m = self.constroi_matriz(self.g_l3)
        self.g_l3_m[2][0] = 1
        self.g_l3_m[2][2] = 1
        self.g_l3_m[3][3] = 1

        # Matriz grafo desconexo
        self.g_d_m = self.constroi_matriz(self.g_d)
        self.g_d_m[0][1] = 1

        # Matriz com ciclo completo
        self.g_c_c_m = self.constroi_matriz(self.g_c_c)
        self.g_c_c_m[0][0] = 1
        self.g_c_c_m[0][1] = 1
        self.g_c_c_m[0][2] = 1
        self.g_c_c_m[1][0] = 1
        self.g_c_c_m[1][1] = 1
        self.g_c_c_m[1][2] = 1
        self.g_c_c_m[2][0] = 1
        self.g_c_c_m[2][1] = 1
        self.g_c_c_m[2][2] = 1

        # Matriz sem arestas
        self.g_c3_m = self.constroi_matriz(self.g_c3)

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1

        # Matrizes geradas
        self.g_a_m = self.constroi_matriz(self.g_a)
        for i in range(len(self.g_a_m)):
            for j in range(len(self.g_a_m)):
                self.g_a_m[i][j] = 1

        self.g_x_m = self.constroi_matriz(self.g_x)
        self.g_x_m[0][1] = 1
        self.g_x_m[0][3] = 1
        self.g_x_m[2][1] = 1
        self.g_x_m[2][3] = 1
        self.g_x_m[3][1] = 1

        self.g_r_m = self.constroi_matriz(self.g_r)
        self.g_r_m[0][0] = 1
        self.g_r_m[0][1] = 1
        self.g_r_m[0][4] = 1
        self.g_r_m[1][0] = 1
        self.g_r_m[1][1] = 1
        self.g_r_m[1][4] = 1
        self.g_r_m[2][3] = 1
        self.g_r_m[4][0] = 1
        self.g_r_m[4][1] = 1
        self.g_r_m[4][4] = 1

        # Grafos desconexos
        self.g_dijkstra = MeuGrafo()
        self.g_dijkstra.adiciona_vertice("A")
        self.g_dijkstra.adiciona_vertice("B")
        self.g_dijkstra.adiciona_vertice("C")
        self.g_dijkstra.adiciona_vertice("D")
        self.g_dijkstra.adiciona_aresta('1', 'A', 'B', 1)
        self.g_dijkstra.adiciona_aresta('2', 'A', 'C', 1)
        self.g_dijkstra.adiciona_aresta('3', 'B', 'D', 1)
        self.g_dijkstra.adiciona_aresta('2', 'C', 'D', 2)

    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g._vertices)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice(
            "C"), self.g_p.get_vertice("Z"))
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

    def test_remove_vertice(self):
        self.assertTrue(self.g_p.remove_vertice("J"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("J")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("K")
        self.assertTrue(self.g_p.remove_vertice("C"))
        self.assertTrue(self.g_p.remove_vertice("Z"))

    def test_remove_aresta(self):
        self.assertTrue(self.g_p.remove_aresta("a1"))
        self.assertFalse(self.g_p.remove_aresta("a1"))
        self.assertTrue(self.g_p.remove_aresta("a7"))
        self.assertFalse(self.g_c.remove_aresta("a"))
        self.assertTrue(self.g_c.remove_aresta("a6"))
        self.assertTrue(self.g_c.remove_aresta("a1", "J"))
        self.assertTrue(self.g_c.remove_aresta("a5", "C"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a2", "X", "C")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", "X")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", v2="X")

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P',
                          'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                          'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), {
            'C-J', 'C-E', 'C-P', 'E-J', 'E-P', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_e.vertices_nao_adjacentes(), {
            'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

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
        self.assertEqual(self.g_e.grau('C'), 5)
        self.assertEqual(self.g_e.grau('D'), 5)

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
        self.assertTrue(self.g_e.ha_paralelas())

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
        self.assertEqual(self.g_e.arestas_sobre_vertice('D'),
                         {'5', '6', '7', '8'})

    def test_eh_completo(self):
        self.assertFalse(self.g_c.eh_completo())
        self.assertFalse(self.g_c2.eh_completo())
        self.assertTrue(self.g_c3.eh_completo())
        self.assertTrue(self.g_c4.eh_completo())

    def test_warshall(self):
        self.assertEqual(self.g_p.warshall(), self.g_p_m)
        self.assertEqual(self.g_e.warshall(), self.g_e_m)
        self.assertEqual(self.g_p_sem_paralelas.warshall(), self.g_p_m2)
        self.assertEqual(self.g_c.warshall(), self.g_c_m)
        self.assertEqual(self.g_l3.warshall(), self.g_l3_m)
        self.assertEqual(self.g_p5.warshall(), self.g_p_m3)
        self.assertEqual(self.g_d.warshall(), self.g_d_m)
        self.assertEqual(self.g_a.warshall(), self.g_a_m)
        self.assertEqual(self.g_x.warshall(), self.g_x_m)
        self.assertEqual(self.g_r.warshall(), self.g_r_m)
        self.assertEqual(self.g_c_c.warshall(), self.g_c_c_m)
        self.assertEqual(self.g_c3.warshall(), self.g_c3_m)

    def test_dijkstra(self):
        self.assertEqual(self.grafo_drone_dijkstra.dijkstra('A', 'Z'), ['A', 'B', 'I', 'J', 'U', 'V', 'Y', 'X', 'Z'])
        self.assertEqual(self.grafo_dijkstra.dijkstra('A', 'E'), ['A', 'B', 'D', 'E'])
        self.assertEqual(self.grafo_dijkstra2.dijkstra('A', 'Z'), ['A', 'B', 'J', 'P', 'U', 'Y', 'Z'])
        self.assertEqual(self.grafo_simples.dijkstra('A', 'C'), ['A', 'B', 'C'])
        self.assertEqual(self.grafo_simples.dijkstra('A', 'D'), ['A', 'D'])
        self.assertEqual(self.grafo_simples.dijkstra('B', 'C'), ['B', 'C'])
        self.assertFalse(self.grafo_simples.dijkstra('B', 'D'))
        self.assertEqual(self.grafo_caminhos_alternativos.dijkstra('A', 'E'), ['A', 'B', 'C', 'D', 'E'])
        self.assertEqual(self.grafo_caminhos_alternativos.dijkstra('B', 'E'), ['B', 'C', 'D', 'E'])
        self.assertEqual(self.grafo_caminhos_alternativos.dijkstra('C', 'E'), ['C', 'D', 'E'])
        self.assertTrue(self.grafo_com_ciclos.dijkstra('A','D') == ['A', 'B', 'C', 'D'] or self.grafo_com_ciclos.dijkstra('A', 'D') == ['A', 'D'])
        self.assertEqual(self.grafo_com_ciclos.dijkstra('B', 'D'), ['B', 'C', 'D'])
        self.assertEqual(self.grafo_complexo.dijkstra('A', 'F'), ['A', 'C', 'E', 'F'])
        self.assertEqual(self.grafo_complexo.dijkstra('B', 'F'), ['B', 'D', 'F'])
        self.assertEqual(self.grafo_complexo.dijkstra('C', 'F'), ['C', 'E', 'F'])
        self.assertEqual(self.grafo_peso_zero.dijkstra('A', 'D'), ['A', 'B', 'C', 'D'])
        self.assertEqual(self.grafo_peso_zero.dijkstra('B', 'D'), ['B', 'C', 'D'])
        self.assertEqual(self.grafo_peso_zero.dijkstra('C', 'D'), ['C', 'D'])


    def test_bellman_ford(self):
        self.assertEqual(self.grafo_drone_bellman.bellman_ford('A', 'Z'), ['A', 'B', 'I', 'J', 'U', 'V', 'Y', 'X', 'Z'])
        self.assertFalse(self.grafo_ciclo_negativo.bellman_ford('A', 'G'))
        self.assertFalse(self.grafo_apenas_ciclos_negativos.bellman_ford('A','C'))
        self.assertFalse(self.grafo_multiplos_ciclos_negativos.bellman_ford('A', 'E'))
        self.assertFalse(self.grafo_ciclo_negativo_multiplo.bellman_ford('A','E'))
        self.assertEqual(self.grafo_sem_ciclo_negativo.bellman_ford('A', 'D'), ['A', 'D'])

