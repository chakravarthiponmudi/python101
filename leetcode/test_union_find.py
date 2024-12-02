import unittest
from UnionFindByRank import UnionFind

class TestUnionFind(unittest.TestCase):
    def test_small_union_find(self):
        uf = UnionFind(10)

        # Initial state, no connections
        for i in range(10):
            self.assertEqual(uf.findRoot(i), i)
            self.assertFalse(uf.isConnected(0, i) if i != 0 else True)

        # Perform some unions
        uf.union(1, 2)
        self.assertTrue(uf.isConnected(1, 2))
        self.assertFalse(uf.isConnected(1, 3))

        uf.union(3, 4)
        uf.union(2, 3)
        self.assertTrue(uf.isConnected(1, 4))
        self.assertTrue(uf.isConnected(2, 4))
        self.assertFalse(uf.isConnected(1, 5))

        # Check path compression
        root1 = uf.findRoot(1)
        root4 = uf.findRoot(4)
        self.assertEqual(root1, root4)

    def test_large_scale_union_find(self):
        size = 100000
        uf = UnionFind(size)

        # Union elements in pairs
        for i in range(0, size, 2):
            uf.union(i, i + 1)

        # Check if pairs are connected
        for i in range(0, size, 2):
            self.assertTrue(uf.isConnected(i, i + 1))
            if i + 2 < size:
                self.assertFalse(uf.isConnected(i, i + 2))

        # Connect everything
        for i in range(size - 1):
            uf.union(i, i + 1)

        # Check if all are connected
        for i in range(size):
            self.assertTrue(uf.isConnected(0, i))

if __name__ == "__main__":
    unittest.main()