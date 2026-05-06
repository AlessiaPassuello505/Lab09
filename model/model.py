import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._grafo=nx.Graph()   #GRAFO NON ORIENTATO
        self._aeroporti=DAO.getAeroporti()
        self._idMapAeroporti={}
        for v in self._aeroporti:
            self._idMapAeroporti[v.ID]=v

    def buildGraphPesato(self,x_soglia):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._aeroporti)
        self.addEdgesPesati(x_soglia)

    def addEdgesPesati(self, x_soglia):
            self._grafo.clear_edges()
            allEdges = DAO.getAllEdgesPesati()  # restituisce (ID_A, ID_B, media)

            for id_a, id_b, media in allEdges:
                # Applichiamo il filtro della soglia x
                if media > x_soglia:
                    # Recuperiamo gli oggetti Aeroporto dalla mappa
                    u = self._idMapAeroporti[id_a]
                    v = self._idMapAeroporti[id_b]
                    # Essendo il grafo (non orientato),
                    # add_edge(u, v) e add_edge(v, u) sono la stessa cosa.
                    self._grafo.add_edge(u, v, weight=media)

    def get_info_grafo(self):
        return len(self._grafo.nodes), len(self._grafo.edges)
