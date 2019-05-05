import networkx as nx
import unittest
from .GN import GN

class TestGN(unittest.TestCase):
    def test_6point(self):
        G=nx.Graph()
        G.add_edge(1,3)
        G.add_edge(1,2)
        G.add_edge(3,2)
        G.add_edge(4,5)
        G.add_edge(4,6)
        G.add_edge(5,6)
        G.add_edge(1,6)     
        self.assertEqual(GN().fit(G).Bestcomps,[{1, 2, 3}, {4, 5, 6}])

if __name__ == '__main__':
    unittest.main()